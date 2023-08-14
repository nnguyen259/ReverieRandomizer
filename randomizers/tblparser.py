from io import BufferedReader
import json
from pathlib import Path
import struct


def get_schema(path: Path):
    with open(path / "schema.json") as jsonfile:
        schemas = json.load(jsonfile)
        tbl_headers = schemas["entries"]
        tbl_commons = schemas["common"]
    return tbl_headers, tbl_commons


def parse_table(table: BufferedReader):
    schemas = get_schema(Path("setup"))
    entry_count = int.from_bytes(table.read(2), "little")
    header_count = int.from_bytes(table.read(4), "little")
    entries = list()
    headers = list()
    for _ in range(header_count):
        header = b""
        header_char = table.read(1)
        while header_char != b"\0":
            header += header_char
            header_char = table.read(1)
        headers.append(header.decode())
        table.read(4)

    for _ in range(entry_count):
        header = b""
        header_char = table.read(1)
        while header_char != b"\0":
            header += header_char
            header_char = table.read(1)
        header = header.decode()
        entries.append(parse_entry(schemas, header, table))
    return {"headers": headers, "entries": entries}


def parse_entry(schemas: tuple[dict, dict], header: str, table: BufferedReader):
    headers, commons = schemas
    schema: dict = headers.get(header)

    entry = dict()
    entry["header"] = header
    entry_length = int.from_bytes(table.read(2), "little")
    if not schema:
        data = table.read(entry_length).hex(" ").upper()
        entry["data"] = data
        return entry

    for key, value in schema.items():
        entry[key] = parse_data(value, table, commons)
    return entry


def parse_data(data_type: str | dict, table: BufferedReader, commons: dict):
    if isinstance(data_type, dict):
        if "bytes" in data_type:
            count = data_type["bytes"]["count"]
            return table.read(count).hex(" ").upper()
        if "repeat" in data_type:
            data = list()
            count = data_type["repeat"]["count"]
            new_type = data_type["repeat"]["type"]
            for _ in range(count):
                data.append(parse_data(new_type, table, commons))
            return data
        if "ref" in data_type:
            data = dict()
            new_header = data_type["ref"]
            schema: dict = commons[new_header]
            for key, value in schema.items():
                data[key] = parse_data(value, table, commons)
            return data

    match data_type:
        case "u8" | "i8":
            return int.from_bytes(table.read(1), "little", signed=data_type.startswith("i"))
        case "u16" | "i16":
            return int.from_bytes(table.read(2), "little", signed=data_type.startswith("i"))
        case "u32" | "i32":
            return int.from_bytes(table.read(4), "little", signed=data_type.startswith("i"))
        case "f32":
            return struct.unpack("<f", table.read(4))[0]
        case "f64":
            return struct.unpack("<d", table.read(8))[0]
        case c if c.startswith("c"):
            encoding = c.split("_")[1]
            result = b""
            character = table.read(1)
            while character != b"\0":
                result += character
                character = table.read(1)
            return result.decode(encoding)
    raise Exception(f"Unknown header {data_type}")


def construct_table(deconstructed_table: dict):
    schemas = get_schema(Path("setup"))

    headers = deconstructed_table["headers"]
    entries = deconstructed_table["entries"]

    header_count = len(headers)
    entry_count = len(entries)

    result = b""
    result += entry_count.to_bytes(2, "little")
    result += header_count.to_bytes(4, "little")

    header_entry_count = dict()
    for header in headers:
        header_entry_count[header] = 0

    entries_data = list()
    for entry in entries:
        entry_data = dict()
        header_name = entry["header"]
        header_entry_count[header_name] += 1

        entry_length, data = construct_entry(schemas, entry)
        entry_data["header"] = header_name
        entry_data["length"] = entry_length
        entry_data["data"] = data
        entries_data.append(entry_data)

    for header_name, length in header_entry_count.items():
        header_name: str
        length: int
        result += header_name.encode("utf8") + b"\0"
        result += length.to_bytes(4, "little")

    for entry_data in entries_data:
        header = entry_data["header"]
        length = entry_data["length"]
        data = entry_data["data"]

        result += header.encode() + b"\0"
        result += length.to_bytes(2, "little")
        result += data

    return result


def construct_entry(schemas: tuple[dict, dict], entry: dict):
    headers, commons = schemas
    header = entry["header"]
    schema: dict = headers.get(header)

    entry_length = 0
    result = b""
    if not schema:
        data = bytes.fromhex(entry["data"])
        result += data
        entry_length = len(data)
        return entry_length, data

    for key, value in schema.items():
        data = construct_data(value, entry[key], commons)
        entry_length += len(data)
        result += data
    return entry_length, result


def construct_data(data_type: str | dict, data: str | int | list | dict, commons: dict):
    if isinstance(data_type, dict):
        if "bytes" in data_type:
            data: str
            return bytes.fromhex(data)
        if "repeat" in data_type:
            data: list
            result = b""
            new_type = data_type["repeat"]["type"]
            for entry in data:
                result += construct_data(new_type, entry, commons)
            return result
        if "ref" in data_type:
            data: dict
            new_header = data_type["ref"]
            schema: dict = commons[new_header]
            result = b""
            for key, value in schema.items():
                result += construct_data(value, data[key], commons)
            return result

    match data_type:
        case "u8" | "i8":
            data: int
            return data.to_bytes(1, "little", signed=data_type.startswith("i"))
        case "u16" | "i16":
            data: int
            return data.to_bytes(2, "little", signed=data_type.startswith("i"))
        case "u32" | "i32":
            data: int
            return data.to_bytes(4, "little", signed=data_type.startswith("i"))
        case "f32":
            data: float
            return struct.pack("<f", data)
        case "f64":
            data: float
            return struct.pack("<d", data)
        case c if c.startswith("c"):
            data: str
            encoding = c.split("_")[1]
            return data.encode(encoding) + b"\0"

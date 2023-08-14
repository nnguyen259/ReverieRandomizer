import json
import random
from pathlib import Path

import randomizers.tblparser as tblparser


def randomize_craft(seed: str, directory: Path):
    random.seed(seed)

    with open("setup/char_moveset.json", "r", encoding="utf8") as movesetfile:
        movesets = json.load(movesetfile)

    with open("setup/upgradeable.json", "r", encoding="utf8") as upgradefile:
        upgrade = json.load(upgradefile)

    with open("setup/solo.json", "r", encoding="utf8") as solofile:
        solo = json.load(solofile)

    random.shuffle(upgrade)
    random.shuffle(solo)

    result = dict()
    result_text = dict()

    for character, moveset in movesets.items():
        result_text[character] = list()
        for animation, moves in moveset.items():
            if len(moves) == 2:
                old_base, old_upgraded = moves
                base, upgraded = upgrade.pop()
                animation = animation if "_" not in animation else animation[:-2]
                result[f"{base[0]}_{base[2]}"] = (old_base[0], old_base[1], old_base[2], old_base[3], old_base[4], animation)
                result[f"{upgraded[0]}_{upgraded[2]}"] = (
                    old_upgraded[0],
                    old_upgraded[1],
                    old_upgraded[2],
                    old_upgraded[3],
                    old_upgraded[4],
                    animation,
                )
                result_text[character].append(f"{old_base[-1]} -> {base[-1]}")
                result_text[character].append(f"{old_upgraded[-1]} -> {upgraded[-1]}")
            else:
                old_base = moves[0]
                base = solo.pop()
                result[f"{base[0]}_{base[2]}"] = (old_base[0], old_base[1], old_base[2], old_base[3], old_base[4], animation)
                result_text[character].append(f"{old_base[-1]} -> {base[-1]}")

    with open(f"results/{seed}/crafts.txt", "w", encoding="utf8") as resultfile:
        resultfile.write(f"Seed: {seed}\n\n")
        for values in result_text.values():
            resultfile.write("\n".join(values))
            resultfile.write("\n")

    with open(directory / "data/text/dat_en/t_magic.tbl", "rb") as magicfile:
        table = tblparser.parse_table(magicfile)

    for entry in table["entries"]:
        if entry["header"] == "magic" and entry["category"] == 30:
            search_id = f"{entry['id']}_{entry['mode_switch']}"
            if new_craft := result.get(search_id):
                entry["id"] = new_craft[0]
                entry["character_restriction"] = new_craft[1]
                entry["mode_switch"] = new_craft[2]
                entry["level_learn"] = new_craft[3]
                entry["sort_id"] = new_craft[4]
                entry["animation"] = new_craft[-1]

    with open(directory / "data/text/dat_en/t_magic.tbl", "wb") as outputfile:
        outputfile.write(tblparser.construct_table(table))


def randomize_order(seed: str, directory: Path, ignore_nadia: bool = False):
    random.seed(seed)

    with open("setup/brave_orders.json", "r", encoding="utf8") as orderfile:
        orders = json.load(orderfile)

    random.shuffle(orders)

    result = f"Seed: {seed}\n\n"

    with open(directory / "data/text/dat_en/t_magic.tbl", "rb") as magicfile:
        table = tblparser.parse_table(magicfile)

    for entry in table["entries"]:
        if entry["header"] == "magic" and entry["category"] == 32 and entry["sub_category"] == 6 and entry["character_restriction"] in range(51):
            if ignore_nadia and entry["name"] == "Analysis Complete!":
                continue
            new_order = orders.pop()
            if ignore_nadia and new_order[-1] == "Analysis Complete!":
                new_order = orders.pop()
            entry["id"] = new_order[0]
            entry["character_restriction"] = new_order[1]
            result += f'{new_order[-1]} -> {entry["name"]}\n'

    with open(f"results/{seed}/orders.txt", "w", encoding="utf8") as resultfile:
        resultfile.write(result)

    with open(directory / "data/text/dat_en/t_magic.tbl", "wb") as outputfile:
        outputfile.write(tblparser.construct_table(table))

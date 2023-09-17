import copy
import random
from pathlib import Path

import kisekiparser.tblparser as tblparser

slot_ids = [2, 3, 4, 5, 6, 7, 8]
slot_ids_reversed = [8, 7, 6, 5, 4, 3, 2]


def randomize_orbment(seed: str, directory: Path, min_line: int = 1, max_line: int = 7, min_color_slot: int = 0, max_color_slot: int = 7):
    print("Starting Orbment Randomizer")
    local_random = random.Random(seed)

    with open(directory / "data/text/dat_en/t_orb.tbl", "rb") as orbfile:
        t_orb = tblparser.parse_table(orbfile)

    results = list()

    for entry in t_orb["entries"]:
        if entry["character"] > 50:
            results.append(entry)

    for i in range(51):
        number_of_line = local_random.randint(min_line, max_line)
        line_setup = list()
        for j in range(number_of_line - 1):
            try:
                line_setup.append(local_random.randint(1, 7 - sum(line_setup) - number_of_line + j))
            except ValueError:
                line_setup.append(1)
        line_setup.append(7 - sum(line_setup))
        local_random.shuffle(line_setup)

        number_of_color = local_random.randint(min_color_slot, max_color_slot)
        elements = list()
        for _ in range(number_of_color):
            elements.append(local_random.randint(1, 7))
        while len(elements) < 7:
            elements.append(0)
        local_random.shuffle(elements)

        results.append({"header": "BaseList", "character": i, "lines": number_of_line, "elements": elements})

        order = copy.deepcopy(local_random.choice([slot_ids, slot_ids_reversed]))
        for j, line_size in enumerate(line_setup):
            setup = list()
            for _ in range(line_size):
                setup.append(order.pop())
            while len(setup) < 7:
                setup.append(-1)

            results.append({"header": "OrbLineList", "character": i, "line": j, "slot_ids": setup})

    t_orb["entries"] = results
    with open(directory / "data/text/dat_en/t_orb.tbl", "wb") as outputfile:
        outputfile.write(tblparser.construct_table(t_orb))

    print("Orbment Randomizer Finished!")


def modify_slot_cost(directory: Path, modifier: float):
    print("Modifying Slot Cost")
    with open(directory / "data/text/dat_en/t_slot.tbl", "rb") as slotfile:
        t_slot = tblparser.parse_table(slotfile)

    for entry in t_slot["entries"]:
        for key in entry:
            if key.endswith("sepith_cost"):
                entry[key] = int(entry[key] * modifier)

    with open(directory / "data/text/dat_en/t_slot.tbl", "wb") as outputfile:
        outputfile.write(tblparser.construct_table(t_slot))

    print("Finished Modifying Slot Cost!")


def modify_quartz_cost(directory: Path, modifier: float):
    print("Modifying Quartz Cost")
    with open(directory / "data/text/dat_en/t_qu_cost.tbl", "rb") as qucost:
        t_qu_cost = tblparser.parse_table(qucost)

    for entry in t_qu_cost["entries"]:
        for key in entry:
            if key.endswith("sepith_cost"):
                entry[key] = int(entry[key] * modifier)

    with open(directory / "data/text/dat_en/t_qu_cost.tbl", "wb") as outputfile:
        outputfile.write(tblparser.construct_table(t_qu_cost))

    print("Finished Modifying Quartz Cost!")

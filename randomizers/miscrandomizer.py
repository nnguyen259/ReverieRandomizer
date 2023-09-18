import json
import random
from pathlib import Path

import kisekiparser.tblparser as tblparser


def remove_trc_floor_req(directory: Path):
    with open(directory / "data/text/dat_en/t_infinity.tbl", "rb") as infinityfile:
        table = tblparser.parse_table(infinityfile)

    for entry in table["entries"]:
        if entry["header"] == "InfinityGachaChara":
            entry["stratum"] = 1

    with open(directory / "data/text/dat_en/t_infinity.tbl", "wb") as outputfile:
        outputfile.write(tblparser.construct_table(table))

    print("Finished Removing Floor Requirement for TRC Chars")


def modify_enemy_variation(directory: Path, min_variation: float = 0.5, max_variation: float = 1.5):
    with open(directory / "data/text/dat_en/t_mons.tbl", "rb") as monsfile:
        table = tblparser.parse_table(monsfile)

    for entry in table["entries"]:
        if entry["header"] == "status" and "R" not in entry["flags"]:
            entry["stat_variation_min"] = min_variation
            entry["stat_variation_max"] = max_variation

    with open(directory / "data/text/dat_en/t_mons.tbl", "wb") as outputfile:
        outputfile.write(tblparser.construct_table(table))

    print("Enemies Stat Variations Increased!")

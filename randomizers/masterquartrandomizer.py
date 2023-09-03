import json
import random
from typing import Literal
import kisekiparser.tblparser as tblparser
from pathlib import Path


def randomize_master_quartz(
    seed: str, directory: Path, randomize_mode: Literal["whole", "slot", "all"] = "whole", selection_mode: Literal["shuffle", "random"] = "shuffle"
):
    print("Starting MQ Abilities Randomizer")
    local_random = random.Random(seed)

    with open("setup/mq_ability_text.json", encoding="utf8") as abilitytextfile:
        master_quartz_ability_text = json.load(abilitytextfile)

    with open("setup/mq_ability_default.json") as defaultfile:
        master_quartz_default = json.load(defaultfile)

    with open("setup/mq_ability_1_data.json") as defaultfile:
        master_quartz_data_1 = json.load(defaultfile)

    with open("setup/mq_ability_2_data.json") as defaultfile:
        master_quartz_data_2 = json.load(defaultfile)

    with open("setup/mq_ability_3_data.json") as defaultfile:
        master_quartz_data_3 = json.load(defaultfile)

    skill_ids = list(master_quartz_default.values())

    new_skill_ids = []
    if randomize_mode == "whole":
        if selection_mode == "shuffle":
            new_skill_ids = skill_ids
            local_random.shuffle(new_skill_ids)
        else:
            new_skill_ids = local_random.choices(skill_ids, k=len(skill_ids))
    elif randomize_mode == "slot":
        skill_1, skill_2, skill_3 = map(list, list(zip(*skill_ids)))
        local_random.shuffle(skill_1)
        local_random.shuffle(skill_2)
        local_random.shuffle(skill_3)

        for _ in range(len(skill_ids)):
            if selection_mode == "shuffle":
                new_skill_ids.append([skill_1.pop(), skill_2.pop(), skill_3.pop()])
            else:
                new_skill_ids.append([local_random.choice(skill_1), local_random.choice(skill_2), local_random.choice(skill_3)])
    else:
        skill_1, skill_2, skill_3 = map(list, list(zip(*skill_ids)))
        skills = []
        skills.extend(skill_1)
        skills.extend(skill_2)
        skills.extend(skill_3)
        local_random.shuffle(skills)

        for _ in range(len(skill_ids)):
            if selection_mode == "shuffle":
                new_skill_ids.append([skills.pop(), skills.pop(), skills.pop()])
            else:
                new_skill_ids.append(local_random.choices(skills, k=3))

    skill_ids = new_skill_ids

    master_quartz_abilities_data = [master_quartz_data_1, master_quartz_data_2, master_quartz_data_3]
    results = dict()

    with open(directory / "data/text/dat_en/t_mstqrt.tbl", "rb") as magicfile:
        table = tblparser.parse_table(magicfile)

    for entry in table["entries"]:
        if entry["header"] == "MasterQuartzBase2":
            item_id = entry["item_id"]
            old_abilities = [entry["ability_1"], entry["ability_2"], entry["ability_1"]]
            new_abilities = skill_ids.pop()

            results[item_id] = [old_abilities, new_abilities]

            entry["ability_1"] = new_abilities[0]
            entry["ability_2"] = new_abilities[1]
            entry["ability_3"] = new_abilities[2]

        if entry["header"] == "MasterQuartzData":
            item_id = entry["item_id"]
            level = entry["level"]
            abilities = results[item_id][1]

            effect_data = list()
            for i, ability in enumerate(abilities):
                if str(ability) in master_quartz_abilities_data[0]:
                    ability_data = master_quartz_abilities_data[0][str(ability)][level - 1]
                elif str(ability) in master_quartz_abilities_data[1]:
                    ability_data = master_quartz_abilities_data[1][str(ability)][level - 1]
                else:
                    ability_data = master_quartz_abilities_data[2][str(ability)][level - 1]
                effect_data.extend(ability_data)
            entry["effect_data"] = effect_data
            entry["memoes"] = [-1] * 9

        if entry["header"] == "MasterQuartzAbilityMemo" and entry["id"] == 57:
            entry["description_2"] = r"Area+%g"

    with open(f"results/{seed}/master_quartz.txt", "w", encoding="utf8") as resultfile:
        for id, abilities in results.items():
            old_abilities, new_abilities = abilities
            resultfile.write(f"{id}:\n")
            for i in range(3):
                resultfile.write(f"{master_quartz_ability_text[str(old_abilities[i])]} -> {master_quartz_ability_text[str(new_abilities[i])]}\n")
            resultfile.write("\n")

    with open(directory / "data/text/dat_en/t_mstqrt.tbl", "wb") as outputfile:
        outputfile.write(tblparser.construct_table(table))

    print("MQ Abilities Randomizer Finished!")


def randomize_master_quartz_stats(seed: str, directory: Path):
    print("Starting MQ Stats Randomizer")
    local_random = random.Random(seed)

    with open(directory / "data/text/dat_en/t_mstqrt.tbl", "rb") as magicfile:
        table = tblparser.parse_table(magicfile)

    for entry in table["entries"]:
        if entry["header"] == "MasterQuartzBase":
            entry["hp_pattern"] = local_random.randint(0, 5)
            entry["ep_pattern"] = local_random.randint(0, 5)
            entry["str_pattern"] = local_random.randint(0, 5)
            entry["def_pattern"] = local_random.randint(0, 5)
            entry["ats_pattern"] = local_random.randint(0, 5)
            entry["adf_pattern"] = local_random.randint(0, 5)
            entry["spd_pattern"] = local_random.randint(0, 5)

    with open(directory / "data/text/dat_en/t_mstqrt.tbl", "wb") as outputfile:
        outputfile.write(tblparser.construct_table(table))

    print("MQ Stats Randomizer Finished!")

import json
import os
import random
import shlex
import shutil
from pathlib import Path
import subprocess

import kisekiparser.tblparser as tblparser


def randomize_model(seed: str, directory: Path):
    print("Starting Model Randomizer")
    shutil.copytree("fix/scripts", directory / "data/scripts", dirs_exist_ok=True)
    local_random = random.Random(seed)

    with open("setup/models.json", encoding="utf8") as modelsfile:
        model_selection = json.load(modelsfile)

    with open("setup/model_list.json", encoding="utf8") as listfile:
        model_list = json.load(listfile)

    selections = list()
    for character in model_selection:
        k = local_random.choice(list(model_selection[character].keys()))
        selections.append((k, model_selection[character][k]))

    local_random.shuffle(selections)
    results = ""

    model_result = dict()
    default_model = dict()
    for character in model_list:
        new_model = selections.pop()
        results += f"{character}: {new_model[0]}\n"
        default_model[model_list[character][0]] = new_model
        model_result[character] = new_model

    with open(directory / "data/text/dat_en/t_attach.tbl", "rb") as attachfile:
        t_attach = tblparser.parse_table(attachfile)

    for entry in t_attach["entries"]:
        if entry["header"] == "AttachTableData" and entry["character"] >= 0 and entry["character"] <= 50 and entry["item_type"] in (5, 9):
            if entry["character"] == 42 and entry["model"] == "C_CHR107_C03":
                continue
            new_model = model_result[str(entry["character"])]
            if entry["item_type"] == 5:
                entry["model"] = new_model[0]
                entry["sprite"] = new_model[1]["cutin"]
                entry["scraft_cutin_id"] = new_model[1]["cutin_id"]
            if entry["item_type"] == 9 and entry["item_id"] == 3207:  # Late game Rean specific
                entry["model"] = new_model[1]["face"]
                entry["scraft_cutin_id"] = new_model[1]["cutin_id"]

    with open(directory / "data/text/dat_en/t_name.tbl", "rb") as namefile:
        t_name = tblparser.parse_table(namefile)

    model_fixes = dict()
    for entry in t_name["entries"]:
        if entry["unknown_string"] != "null" and entry["model"] in default_model:
            new_model = default_model[entry["model"]]
            if entry["animation"] not in model_fixes:
                model_fixes[entry["animation"]] = new_model[0]
            entry["model"] = new_model[0]
            entry["default_face"] = new_model[1]["default_face"]
            entry["face"] = new_model[1]["face"]
            continue
        if entry["character"] >= 0 and entry["character"] <= 50:
            new_model = model_result[str(entry["character"])]
            if entry["animation"] not in model_fixes:
                model_fixes[entry["animation"]] = new_model[0]
            entry["model"] = new_model[0]
            entry["default_face"] = new_model[1]["default_face"]
            entry["face"] = new_model[1]["face"]
            entry["face"] = new_model[1]["face"]
            continue

    fix_models(model_fixes, directory)

    with open(f"results/{seed}/models.txt", "w", encoding="utf8") as resultfile:
        resultfile.write(results)

    with open(directory / "data/text/dat_en/t_attach.tbl", "wb") as attachfile:
        attachfile.write(tblparser.construct_table(t_attach))

    with open(directory / "data/text/dat_en/t_name.tbl", "wb") as namefile:
        namefile.write(tblparser.construct_table(t_name))

    print("Model Randomizer Finished!")


def fix_models(model_fixes: dict, directory: Path):
    os.makedirs(f"tmp/model_fix", exist_ok=True)
    shutil.copytree("fix/py", "tmp/model_fix", dirs_exist_ok=True)
    shutil.copy("kisekiparser/py2scena.exe", "tmp/model_fix/py2scena.exe")

    current_dir = Path.cwd()
    os.chdir("tmp/model_fix")
    for file, model in model_fixes.items():
        print(f"Fixing model {file}")
        with open(f"{file}.py", encoding="utf8") as inputfile:
            data = inputfile.read()
        data = data.replace("PLACEHOLDER_REPLACE", model)
        with open(f"{file}.py", "w", encoding="utf8") as outputfile:
            outputfile.write(data)
        subprocess.run(shlex.split(f"py2scena.exe {file}.py"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        shutil.copy(f"{file}.dat", directory / "data/scripts/ani/dat_en")

    os.chdir(current_dir)

    shutil.rmtree("tmp/model_fix")

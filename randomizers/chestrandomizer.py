import json
import os
import random
import shlex
import shutil
import subprocess
import multiprocessing
from pathlib import Path

import libcst
from libcst._flatten_sentinel import FlattenSentinel
from libcst._nodes.statement import BaseStatement, FunctionDef
from libcst._removal_sentinel import RemovalSentinel


# fmt: off
master_quartz = [3607, 3598, 3593, 3599, 3594, 3600, 3606, 3614, 3605, 3640, 3613, 3624, 3603, 3592]

multi_chest_options = [(300, 300), (310, 3000), (311, 3000), (312, 3000), (313, 3000), (314, 3000), (315, 3000), (316, 3000),
                       (303, 200), (50, 40), (51, 40), (52, 40), (53, 40), (54, 40)]

chest_chances = [[40, 35, 10, 5, 5, 5],
                 [20, 40, 20, 10, 5, 5],
                 [0, 20, 40, 20, 15, 5],
                 [0, 0, 10, 50, 35, 5],
                 [0, 0, 0, 30, 65, 5]]


# fmt: on
class ChestVisitor(libcst.CSTTransformer):
    def __init__(self, single_chest_items: list, multi_chest_items: list, randomizer: random.Random) -> None:
        super().__init__()
        self.single_chest_items = single_chest_items
        self.multi_chest_items = multi_chest_items
        self.chest_index = dict()
        self.randomizer = randomizer

    def leave_Call(self, original_node: libcst.Call, updated_node: libcst.Call):
        if original_node.func.value == "ModelCmd" and original_node.args[0].value.value == "0x0D":
            if original_node.args[2].value.value == "''":
                if original_node.args[1].value.value in self.chest_index:
                    new_arg = libcst.Arg(libcst.Integer(self.chest_index[original_node.args[1].value.value]))
                else:
                    new_value = str(self.single_chest_items.pop())
                    new_arg = libcst.Arg(libcst.Integer(new_value))
                    self.chest_index[original_node.args[1].value.value] = new_value
                args = list(updated_node.args)[0:4]
                args.append(new_arg)
                new_node = updated_node.with_changes(args=args)
                return new_node
            else:
                return updated_node
        return updated_node

    def leave_FunctionDef(
        self, original_node: libcst.FunctionDef, updated_node: FunctionDef
    ) -> BaseStatement | FlattenSentinel[BaseStatement] | RemovalSentinel:
        if original_node.name.value.startswith("LP_tbox"):
            new_body: list[BaseStatement] = list()
            items = list()

            for statement in original_node.body.body:
                expr: libcst.Call = statement.body[0].value
                if expr.func.value == "AddItem":
                    item = self.randomizer.choice(self.multi_chest_items)
                    items.append(item)
                    item_id, item_count = item
                    new_args = list()
                    new_call = expr.with_changes(args=new_args)
                    new_args.append(expr.args[0])
                    new_args.append(expr.args[1].with_changes(value=libcst.Integer(str(item_id))))
                    new_args.append(libcst.Arg(libcst.Integer(str(item_count))))
                    new_body.append(libcst.SimpleStatementLine([libcst.Expr(new_call)]))
                elif expr.func.value == "Talk":
                    new_args = list()
                    new_args.append(expr.args[0])
                    new_elements = list()

                    for element in expr.args[1].value.elements:
                        if isinstance(element.value, libcst.SimpleString):
                            element_string: libcst.SimpleString = element.value
                            if "Obtained" in element_string.value:
                                new_elements.append(element)
                                continue
                            if element_string.value.endswith("n'"):
                                new_string = rf"' x{item[1]}\n'"
                                new_elements.append(element.with_changes(value=libcst.SimpleString(new_string)))
                            else:
                                new_string = rf"' x{item[1]}'"
                                new_elements.append(element.with_changes(value=libcst.SimpleString(new_string)))
                        elif isinstance(element.value, libcst.Tuple):
                            element_tuple: libcst.Tuple = element.value
                            item = items.pop()
                            new_element = list()
                            new_element.append(element_tuple.elements[0])
                            new_element.append(libcst.Element(libcst.Integer(str(item[0]))))
                            new_elements.append(element.with_changes(value=libcst.Tuple(new_element)))
                        else:
                            new_elements.append(element)
                    new_tuple = expr.args[1].value.with_changes(elements=new_elements)
                    new_args.append(expr.args[1].with_changes(value=new_tuple))
                    new_call = expr.with_changes(args=new_args)

                    new_body.append(libcst.SimpleStatementLine([libcst.Expr(new_call)]))
                else:
                    new_body.append(statement)
            new_node = updated_node.with_changes(body=libcst.IndentedBlock(new_body))
            return new_node
        return updated_node


def do_randomize(seed: str, directory: Path, visitor: ChestVisitor, maps: list):
    for map_name in maps:
        print(f"Current map={map_name}")

        shutil.copy(directory / f"data/scripts/scena/dat_en/{map_name}.dat", f"{map_name}.dat")

        subprocess.run(shlex.split(f"scena2py.exe {map_name}.dat"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.remove(f"{map_name}.dat")
        with open(f"{map_name}.py", encoding="utf") as mapfile:
            map_cst = libcst.parse_module(mapfile.read())

        map_cst = map_cst.visit(visitor)
        with open(f"{map_name}.py", "w", encoding="utf") as mapfile:
            mapfile.write(map_cst.code)

        subprocess.run(shlex.split(f"py2scena.exe {map_name}.py"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.remove(f"{map_name}.py")

        shutil.copy(f"{map_name}.dat", directory / f"data/scripts/scena/dat_en/{map_name}.dat")


def randomize_chest(seed: str, directory: Path):
    print("Starting Chests Randomizer")
    local_random = random.Random(seed)
    local_random.shuffle(master_quartz)
    processes = list()
    single_items = list()

    with open("setup/chests.json") as chestfile:
        chests = json.load(chestfile)

    with open("setup/items.json", encoding="utf8") as itemfile:
        item_ids = json.load(itemfile)

    for i in range(1, 7):
        with open(f"setup/tier{i}_items.json", encoding="utf8") as itemfile:
            single_items.append(json.load(itemfile))

    current_dir = Path.cwd()
    shutil.rmtree(f"tmp/{seed}", ignore_errors=True)
    os.makedirs(f"tmp/{seed}", exist_ok=True)
    shutil.copy("kisekiparser/scena2py.exe", f"tmp/{seed}/scena2py.exe")
    shutil.copy("kisekiparser/py2scena.exe", f"tmp/{seed}/py2scena.exe")
    os.chdir(f"tmp/{seed}")

    for i, act in enumerate(chests):
        maps, single_chests, _, chest_tier = list(zip(*act))
        total_chests = sum(single_chests)
        chest_tier = chest_tier[0]
        chest_rate = chest_chances[chest_tier - 1]
        chest_pool = list()
        tiers = local_random.choices([0, 1, 2, 3, 4, 5], weights=chest_rate, k=total_chests - 1)
        for tier in tiers:
            item_pool = single_items[tier]
            category = local_random.choices(list(item_pool["categories"].keys()), weights=item_pool["odds"], k=1)[0]
            chest_pool.append(item_ids[local_random.choice(item_pool["categories"][category])])
        chest_pool.append(master_quartz.pop())
        local_random.shuffle(chest_pool)
        visitor = ChestVisitor(chest_pool, multi_chest_options, random.Random(f"{seed}_{i}"))
        process = multiprocessing.Process(target=do_randomize, args=[seed, directory, visitor, maps])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    os.chdir(current_dir)
    shutil.rmtree(f"tmp/{seed}")

    print("Chests Randomizer Finished!")

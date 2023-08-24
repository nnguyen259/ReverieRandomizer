import json
import os
import random
import shlex
import shutil
import subprocess
import time
import multiprocessing
from pathlib import Path

import libcst
from libcst._flatten_sentinel import FlattenSentinel
from libcst._nodes.statement import BaseStatement, FunctionDef
from libcst._removal_sentinel import RemovalSentinel


# fmt: off
master_quartz = [3607, 3598, 3593, 3599, 3594, 3600, 3606, 3614, 3605, 3640, 3613, 3624, 3603, 3592]
single_chest_options = [3748, 3749, 3750, 3751, 3752, 3753, 3754, 3755,
                        3820, 3821, 3822, 3823, 3824, 3825, 3826, 3827, 3828, 3829,
                        3887, 3888, 3889, 3890, 3891, 3892, 3893, 3894,
                        3951, 3952, 3953, 3954, 3955, 3956, 3957,
                        4007, 4008, 4009, 4010, 4011, 4012, 
                        4062, 4063, 4064, 4065, 4066, 4067,
                        4118, 4119, 4120, 4121, 4122, 4123,
                        3760, 3759, 3761, 3762, 3763, 3764, 3765,
                        3834, 3833, 3835, 3837, 3836, 3838,
                        3899, 3898, 3900, 3901, 3902, 3903, 3904, 3905,
                        3962, 3961, 3964, 3963, 3965, 3966, 3967,
                        4016, 4015, 4017, 4018, 4019, 4020, 4021,
                        4070, 4071, 4069, 4072, 4073, 4074, 4075, 4076,
                        4132, 4126, 4127, 4128, 4130, 4129, 4131,
                        302, 15, 16, 17, 18, 20, 21, 61, 62, 63,
                        2612, 2613, 2616, 2617, 2620, 2621, 2624, 2625, 2628, 2629, 2632, 2633, 2636, 2637,
                        2640, 2641, 2644, 2645, 2648, 2649, 2652, 2653, 2656, 2657, 2660, 2661, 2664, 2665,
                        2668, 2669, 2672, 2673, 2676, 2677, 2680, 2681, 2684, 2685, 2686, 2689, 2690, 2691,
                        2692, 2693, 2694, 2716, 2731, 2740, 2741, 2742, 2743, 2744, 2745, 2746, 2747]

multi_chest_options = [(300, 300), (310, 3000), (311, 3000), (312, 3000), (313, 3000), (314, 3000), (315, 3000), (316, 3000),
                       (300, 300), (310, 3000), (311, 3000), (312, 3000), (313, 3000), (314, 3000), (315, 3000), (316, 3000),
                       (300, 300), (310, 3000), (311, 3000), (312, 3000), (313, 3000), (314, 3000), (315, 3000), (316, 3000),
                       (3, 10), (8, 10), (11, 5), (37, 5), (50, 10), (51, 10), (52, 10), (53, 10), (54, 10), (58, 3), (59, 3), (60, 3),
                       (3737, 2), (3738, 2), (3756, 2), (3757, 2), (3758, 2),
                       (3809, 2), (3810, 2), (3830, 2), (3831, 2), (3832, 2),
                       (3876, 2), (3877, 2), (3895, 2), (3896, 2), (3897, 2),
                       (3939, 2), (3940, 2), (3958, 2), (3959, 2), (3960, 2),
                       (3997, 2), (3998, 2), (4013, 2), (4014, 2),
                       (4051, 2), (4052, 2), (4054, 2), (4068, 2),
                       (4107, 2), (4108, 2), (4124, 2), (4125, 2)]


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
    local_random = random.Random(seed)
    local_random.shuffle(master_quartz)
    processes = list()

    with open("setup/chests.json") as chestfile:
        chests = json.load(chestfile)

    current_dir = Path.cwd()
    shutil.rmtree(f"tmp/{seed}", ignore_errors=True)
    os.makedirs(f"tmp/{seed}", exist_ok=True)
    shutil.copy("kisekiparser/scena2py.exe", f"tmp/{seed}/scena2py.exe")
    shutil.copy("kisekiparser/py2scena.exe", f"tmp/{seed}/py2scena.exe")
    os.chdir(f"tmp/{seed}")

    for i, act in enumerate(chests):
        maps, single_chests, _ = list(zip(*act))
        total_chests = sum(single_chests)
        chest_pool = random.choices(single_chest_options, k=total_chests - 1)
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

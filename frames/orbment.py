from pathlib import Path
from tkinter import ttk
import tkinter

import randomizers.orbmentrandomizer as randomizer


class OrbmentRandomizerFrame(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master, text="Orbment")
        self.columnconfigure(0, weight=1)

        self.randomize_orbment = tkinter.BooleanVar()
        self.randomize_orbment_button = ttk.Checkbutton(self, text="Randomize Orbments", variable=self.randomize_orbment)
        self.randomize_orbment_button.grid(row=0, column=0, sticky="w")

        self.min_line = tkinter.IntVar()
        self.min_line.set(1)
        ttk.Label(self, text="Min Number of Line (1-7)").grid(row=1, column=0, sticky="w")
        ttk.Spinbox(self, width=5, from_=1, to=7, increment=1, wrap=True, textvariable=self.min_line).grid(row=1, column=1, sticky="w")

        self.max_line = tkinter.IntVar()
        self.max_line.set(4)
        ttk.Label(self, text="Max Number of Line (1-7)").grid(row=2, column=0, sticky="w")
        ttk.Spinbox(self, width=5, from_=1, to=7, increment=1, wrap=True, textvariable=self.max_line).grid(row=2, column=1, sticky="w")

        self.min_element = tkinter.IntVar()
        self.min_element.set(3)
        ttk.Label(self, text="Min Number of Elemental Slot (0-7)").grid(row=3, column=0, sticky="w")
        ttk.Spinbox(self, width=5, from_=0, to=7, increment=1, wrap=True, textvariable=self.min_element).grid(row=3, column=1, sticky="w")

        self.max_element = tkinter.IntVar()
        self.max_element.set(3)
        ttk.Label(self, text="Max Number of Elemental Slot (0-7)").grid(row=4, column=0, sticky="w")
        ttk.Spinbox(self, width=5, from_=0, to=7, increment=1, wrap=True, textvariable=self.max_element).grid(row=4, column=1, sticky="w")

        self.modify_slot_cost = tkinter.BooleanVar()
        self.modify_slot_cost_button = ttk.Checkbutton(self, text="Modify Slot Sepith Cost", variable=self.modify_slot_cost)
        self.modify_slot_cost_button.grid(row=5, column=0, sticky="w")

        self.slot_modifier = tkinter.DoubleVar()
        self.slot_modifier.set(1.0)
        ttk.Label(self, text="Slot Sepith Cost Multiplier (0.0-2.0)").grid(row=6, column=0, sticky="w")
        ttk.Spinbox(self, width=5, from_=0.0, to=2.0, increment=0.1, wrap=True, textvariable=self.slot_modifier).grid(row=6, column=1, sticky="w")

        self.modify_quartz_cost = tkinter.BooleanVar()
        self.modify_quartz_cost_button = ttk.Checkbutton(self, text="Modify Quartz Sepith Cost", variable=self.modify_quartz_cost)
        self.modify_quartz_cost_button.grid(row=7, column=0, sticky="w")

        self.quartz_modifier = tkinter.DoubleVar()
        self.quartz_modifier.set(1.0)
        ttk.Label(self, text="Quartz Sepith Cost Multiplier (0.0-2.0)").grid(row=8, column=0, sticky="w")
        ttk.Spinbox(self, width=5, from_=0.0, to=2.0, increment=0.1, wrap=True, textvariable=self.quartz_modifier).grid(row=8, column=1, sticky="w")

        for slave in self.grid_slaves():
            slave.grid_configure(padx=15)

    def randomize(self, seed, directory: Path):
        if self.randomize_orbment.get():
            min_line = self.min_line.get()
            max_line = self.max_line.get()
            if min_line > max_line:
                min_line, max_line = max_line, min_line

            min_element = self.min_element.get()
            max_element = self.max_element.get()
            if min_element > max_element:
                min_element, max_element = max_element, min_element

            randomizer.randomize_orbment(seed, directory, min_line, max_line, min_element, max_element)
        if self.modify_slot_cost.get():
            randomizer.modify_slot_cost(directory, self.slot_modifier.get())
        if self.modify_quartz_cost.get():
            randomizer.modify_quartz_cost(directory, self.quartz_modifier.get())

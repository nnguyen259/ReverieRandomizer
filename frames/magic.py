from pathlib import Path
from tkinter import ttk
import tkinter
import randomizers.craftrandomizer as randomizer


class CraftRandomizerFrame(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master, text="Crafts & Orders")
        self.columnconfigure(0, weight=1)

        self.randomize_craft = tkinter.BooleanVar()
        self.randomize_craft_button = ttk.Checkbutton(self, text="Randomize Crafts", variable=self.randomize_craft)
        self.randomize_craft_button.grid(row=0, column=0, sticky="w")

        self.randomize_order = tkinter.BooleanVar()
        self.randomize_order_button = ttk.Checkbutton(self, text="Randomize Brave Orders", variable=self.randomize_order)
        self.randomize_order_button.grid(row=0, column=1, sticky="w")

        self.ignore_nadia = tkinter.BooleanVar()
        self.ignore_nadia_button = ttk.Checkbutton(self, text="Ignore Analysis Complete", variable=self.ignore_nadia)
        self.ignore_nadia_button.grid(row=1, column=1, sticky="w")

        for slave in self.grid_slaves():
            slave.grid_configure(padx=15)

        self.ignore_nadia_button.grid_configure(padx=30)

    def randomize(self, seed, directory: Path):
        if self.randomize_craft.get():
            randomizer.randomize_craft(seed, directory)
        if self.randomize_order.get():
            randomizer.randomize_order(seed, directory, self.ignore_nadia.get())

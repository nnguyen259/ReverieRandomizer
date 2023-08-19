from pathlib import Path
from tkinter import ttk
import tkinter
import randomizers.masterquartrandomizer as randomizer


class MasterQuartzRandomizerFrame(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master, text="Master Quartz")
        self.columnconfigure(0, weight=1)

        self.randomize_stat = tkinter.BooleanVar()
        self.randomize_stat_button = ttk.Checkbutton(self, text="Randomize Stats", variable=self.randomize_stat)
        self.randomize_stat_button.grid(row=0, column=0, sticky="w")

        self.randomize_ability = tkinter.BooleanVar()
        self.randomize_ability_button = ttk.Checkbutton(self, text="Randomize Abilities", variable=self.randomize_ability)
        self.randomize_ability_button.grid(row=1, column=0, sticky="w")

        ttk.Label(self, text="Randomize Mode").grid(row=2, column=0, sticky="w")
        self.randomize_mode = tkinter.StringVar()
        self.randomize_mode.set("whole")
        ttk.Radiobutton(self, text="Whole Master Quartz", variable=self.randomize_mode, value="whole").grid(row=3, column=0, sticky="w")
        ttk.Radiobutton(self, text="Same Slot Abilities", variable=self.randomize_mode, value="slot").grid(row=4, column=0, sticky="w")
        ttk.Radiobutton(self, text="All Abilities", variable=self.randomize_mode, value="all").grid(row=5, column=0, sticky="w")

        ttk.Label(self, text="Random Selection Mode").grid(row=2, column=1, sticky="w")
        self.selection_mode = tkinter.StringVar()
        self.selection_mode.set("shuffle")
        ttk.Radiobutton(self, text="Shuffle", variable=self.selection_mode, value="shuffle").grid(row=3, column=1, sticky="w")
        ttk.Radiobutton(self, text="Random", variable=self.selection_mode, value="random").grid(row=4, column=1, sticky="w")

        for slave in self.grid_slaves():
            slave.grid_configure(padx=15)

    def randomize(self, seed, directory: Path):
        if self.randomize_ability.get():
            randomizer.randomize_master_quartz(seed, directory, self.randomize_mode.get(), self.selection_mode.get())

        if self.randomize_stat.get():
            randomizer.randomize_master_quartz_stats(seed, directory)

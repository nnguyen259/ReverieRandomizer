from pathlib import Path
from tkinter import ttk
import tkinter
import randomizers.chestrandomizer as chest_randomizer
import randomizers.modelrandomizer as model_randomizer


class ExperimentalFrame(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master, text="Experimental Features")
        self.columnconfigure(0, weight=1)

        self.randomize_chest = tkinter.BooleanVar()
        self.randomize_chest_button = ttk.Checkbutton(self, text="Randomize Chests", variable=self.randomize_chest)
        self.randomize_chest_button.grid(row=0, column=0, sticky="w")

        self.randomize_model = tkinter.BooleanVar()
        self.randomize_model_button = ttk.Checkbutton(self, text="Randomize Models", variable=self.randomize_model)
        self.randomize_model_button.grid(row=1, column=0, sticky="w")

        for slave in self.grid_slaves():
            slave.grid_configure(padx=15)

    def randomize(self, seed, directory: Path):
        if self.randomize_model.get():
            model_randomizer.randomize_model(seed, directory)
        if self.randomize_chest.get():
            chest_randomizer.randomize_chest(seed, directory)

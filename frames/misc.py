from pathlib import Path
from tkinter import ttk
import tkinter
import randomizers.chestrandomizer as chest_randomizer
import randomizers.modelrandomizer as model_randomizer
import randomizers.miscrandomizer as misc_randomizer


class MiscFrame(ttk.Labelframe):
    def __init__(self, master):
        super().__init__(master, text="Misc Features")
        self.columnconfigure(0, weight=1)

        self.randomize_chest = tkinter.BooleanVar()
        self.randomize_chest_button = ttk.Checkbutton(self, text="Randomize Chests", variable=self.randomize_chest)
        self.randomize_chest_button.grid(row=0, column=0, sticky="w")

        self.randomize_model = tkinter.BooleanVar()
        self.randomize_model_button = ttk.Checkbutton(self, text="Randomize Models", variable=self.randomize_model)
        self.randomize_model_button.grid(row=1, column=0, sticky="w")

        self.unlock_trc_char = tkinter.BooleanVar()
        self.unlock_trc_char_button = ttk.Checkbutton(self, text="Remove TRC Chars Floor Requirement", variable=self.unlock_trc_char)
        self.unlock_trc_char_button.grid(row=2, column=0, sticky="w")

        self.increase_enemy_variation = tkinter.BooleanVar()
        self.increase_enemy_variation_button = ttk.Checkbutton(self, text="Increase Enemies Stat Variation", variable=self.increase_enemy_variation)
        self.increase_enemy_variation_button.grid(row=3, column=0, sticky="w")

        for slave in self.grid_slaves():
            slave.grid_configure(padx=15)

    def randomize(self, seed, directory: Path):
        if self.randomize_model.get():
            model_randomizer.randomize_model(seed, directory)
        if self.randomize_chest.get():
            chest_randomizer.randomize_chest(seed, directory)
        if self.unlock_trc_char.get():
            misc_randomizer.remove_trc_floor_req(directory)
        if self.increase_enemy_variation.get():
            misc_randomizer.modify_enemy_variation(directory)

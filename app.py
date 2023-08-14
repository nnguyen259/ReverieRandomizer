import os
from pathlib import Path
import tkinter
from tkinter import ttk
from tkinter import filedialog, messagebox

from frames.generalinfo import GeneralInfoFrame
from frames.magic import CraftRandomizerFrame


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reverie Randomizer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.general_frame = GeneralInfoFrame(self)
        self.general_frame.grid(row=0, column=0, sticky="nsew")

        self.randomizers = ttk.Frame(self)
        self.randomizers.grid(row=1, column=0, sticky="nsew")

        CraftRandomizerFrame(self.randomizers).pack(expand=True, fill="both")

        self.randomize_button = ttk.Button(self, text="Randomize!", command=self.randomize)
        self.randomize_button.grid(row=2, column=0, pady=10)

    def randomize(self):
        directory, seed = self.general_frame.get_value()

        if not directory:
            messagebox.showerror("No Directory", "No Game Directory Selected. Aborting...")
            return

        os.makedirs(f"results/{seed}", exist_ok=True)
        self.randomize_button["state"] = "disabled"
        for randomizer in self.randomizers.pack_slaves():
            randomizer.randomize(seed, Path(directory))
        self.randomize_button["state"] = "normal"
        messagebox.showinfo("Finished!", "All Done!")


app = App()
app.mainloop()

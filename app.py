import os
import threading
import tkinter
from multiprocessing import freeze_support
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from frames.misc import MiscFrame
from frames.generalinfo import GeneralInfoFrame
from frames.magic import CraftRandomizerFrame
from frames.masterquartz import MasterQuartzRandomizerFrame
from frames.orbment import OrbmentRandomizerFrame


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
        MasterQuartzRandomizerFrame(self.randomizers).pack(expand=True, fill="both")
        OrbmentRandomizerFrame(self.randomizers).pack(expand=True, fill="both")
        MiscFrame(self.randomizers).pack(expand=True, fill="both")

        self.randomize_button = ttk.Button(self, text="Randomize!", command=self.randomize)
        self.randomize_button.grid(row=2, column=0, pady=10)

    def randomize(self):
        def _randomize():
            directory, seed = self.general_frame.get_value()

            if not directory:
                messagebox.showerror("No Directory", "No Game Directory Selected. Aborting...")
                return

            self.general_frame.status.set("Randomizing...")
            print("Starting Randomizer")
            os.makedirs(f"results/{seed}", exist_ok=True)
            for randomizer in self.randomizers.pack_slaves():
                randomizer.randomize(seed, Path(directory))
            self.randomize_button["state"] = "normal"
            print("Randomizing Done!")
            self.general_frame.status.set("All Done!")
            messagebox.showinfo("Finished!", "All Done!")

        self.randomize_button["state"] = "disabled"
        threading.Thread(target=_randomize).start()


if __name__ == "__main__":
    freeze_support()
    app = App()
    app.mainloop()

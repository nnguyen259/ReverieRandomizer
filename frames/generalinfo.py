import os
import random
import string
import tkinter
from tkinter import ttk
from tkinter import filedialog, messagebox


class GeneralInfoFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure(1, weight=1)

        self.directory_label = ttk.Label(self, text="Game Directory:")
        self.directory_label.grid(row=0, column=0, sticky="w")

        self.directory = ttk.Entry(self)
        self.directory.grid(row=0, column=1, sticky="ew")

        self.directory_browse = ttk.Button(self, text="Browse", command=self.select_directory)
        self.directory_browse.grid(row=0, column=2)

        self.seed_label = ttk.Label(self, text="Seed:")
        self.seed_label.grid(row=1, column=0, sticky="w")

        self.seed = ttk.Entry(self)
        self.seed.grid(row=1, column=1, sticky="ew")

        self.status = tkinter.StringVar()
        self.status.set("Ready")
        self.status_label = ttk.Label(self, textvariable=self.status)
        self.status_label.grid(row=1, column=2)

        for slave in self.grid_slaves():
            slave.grid_configure(padx=15, pady=5)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if "data" not in os.listdir(directory):
            messagebox.showerror(title="Invalid Game Directory", message="Please Select a Valid Game Directory")
        else:
            self.directory.delete(0)
            self.directory.insert(0, directory)

    def get_value(self):
        if not self.seed.get():
            seed = "".join(random.choices(string.ascii_letters + string.digits, k=10))
            self.seed.insert(0, seed)
        return self.directory.get(), self.seed.get()

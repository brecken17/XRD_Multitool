import tkinter as tk
from tkinter import Tk, ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import crystalpeaktab as cp
import smallangletab as sa
matplotlib.use("TkAgg")

class mainwin:
    def __init__(self, master):
        self.master = master
        master.title
        master.title("University of Utah XRD Analysis Multi-tool")
        #Sets up tabs
        self.tab_parent = ttk.Notebook(master)
        self.tab1 = ttk.Frame(self.tab_parent)
        self.tab2 = ttk.Frame(self.tab_parent)
        self.tab3 = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.tab1, text="Crystallization Peak Fit")
        self.tab_parent.add(self.tab2, text="Small Angle Simulation")
        self.tab_parent.grid(row=1, column=0)
        # Spacers
        tk.Label(self.master, text="").grid(row=2, column=3)
        # Sets the first tab to be the crystal peak analysis
        cp.tab(self.tab1)
        # Sets the second tab to be the Small Angle Analytic Simulation
        sa.tab(self.tab2)
# ======================================================================================================================
# ======================================================================================================================
# MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN  MAIN MAIN  MAIN  MAIN  MAIN  MAIN  MAIN MAIN  MAIN  MAIN
# ======================================================================================================================
root = tk.Tk()
my_gui = mainwin(root)
root.mainloop()
# ======================================================================================================================
# ======================================================================================================================

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

from crystalpeaktab import *
from ScrollableFrame import *
from datahandling import *
matplotlib.use("TkAgg")


class tab():
    def __init__(self, tab):
        self.nfiles = 1  # The default number of data file
        self.nbrframe = tab
        self.nbrframelabel = tk.Label(self.nbrframe, text="Utah - LIGO: Crystallization Peak Analysis",
                              font=("Helvetica", 24)).grid(row=0, columnspan=5)
        tk.Label(self.nbrframe, text='----------------------------------------------------------------------------------'
                                     '-----------------------------------------------------------------').grid(row=1,
                                                                                                         columnspan=5)
        # Plot style
        LARGE_FONT = ("Verdana", 12)
        style.use("ggplot")
        # Establishes figure and subplot
        self.f2 = Figure(figsize=(4, 4), dpi=100)
        self.a2 = self.f2.add_subplot(111)
        # creates and positions a canvas using the figure f
        self.canvas2 = FigureCanvasTkAgg(self.f2, self.nbrframe)
        self.canvas2.get_tk_widget().grid(row=2, columnspan=5)

        ###############    TOOLBAR    ###############
        self.toolbarFrame2 = tk.Frame(self.nbrframe)
        self.toolbarFrame2.grid(row=3, columnspan=5)
        self.toolbar2 = NavigationToolbar2Tk(self.canvas2, self.toolbarFrame2)

        self.xleftentry = tk.Entry(self.nbrframe, width=10)
        self.xleftentry.grid(row=4, column=1)
        self.xrightentry = tk.Entry(self.nbrframe, width=10)
        self.xrightentry.grid(row=4, column=2)

        # Frame for selecting number of files

        self.fileframe = tk.Frame(self.nbrframe)
        self.fileframe.grid(row=5, columnspan=5)
        # Button to decrement the number of files
        self.minusbuttonphoto = tk.PhotoImage(file=r"Pictures/decreasefileicon.png")
        self.minusbuttonimage = self.minusbuttonphoto.subsample(15, 15)
        self.decrease_button = tk.Button(self.fileframe, image=self.minusbuttonimage,
                                 activebackground='grey50', command=self.decrease)
        self.decrease_button.grid(row=1, column=0)
        # Label to display the number of files
        self.plan = tk.Label(self.fileframe,
                     text="Compare " + str(self.nfiles) + " files",
                     font=("Arial Bold", 16))
        self.plan.grid(row=1, column=1)
        # Button to increment the number of files
        self.plusbuttonphoto = tk.PhotoImage(file=r"Pictures/increasefileicon.png")
        self.plusbuttonimage = self.plusbuttonphoto.subsample(15, 15)
        self.increase_button = tk.Button(self.fileframe, image=self.plusbuttonimage,
                                 activebackground='grey50', command=self.increase)
        self.increase_button.grid(row=1, column=2)

        self.filesframe = ScrollableFrame(self.nbrframe)
        self.filesframe.grid(row=6, column=3)
        self.addbutton = tk.Button(self.filesframe.scrollable_frame, text='Add File', command=self.increase)
        self.addbutton.grid(row=100, column=0)
        self.deletefilesbutton = tk.Button(self.filesframe.scrollable_frame, text='Delete', command=self.decrease)
        self.deletefilesbutton.grid(row=100, column=1)
        tk.Label(self.nbrframe, text="").grid(row=7, column=1)
        tk.Label(self.nbrframe, text="").grid(row=8, column=1)

        self.files = []
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Scrollbar frame that allows the selection of data files

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def increase(self):
        # Invoked when the increase button is clicked.
        # It increment the number of data files
        # It updates the label displaying the number of files.
        if (self.nfiles < 8):
            self.nfiles = self.nfiles + 1
            self.plan.configure(text="Compare " + str(self.nfiles) + " files")
        self.choosefile = tk.Button(self.filesframe.scrollable_frame, text="Choose data",
                                    command=lambda: choosedatafile(self.choosefile_lbl, self.files)
                                     ).grid(row=np.int(self.nfiles), column=0)
        # Data file label
        self.choosefile_lbl = tk.Label(self.filesframe.scrollable_frame, text='-', font=("Arial Bold", 8),
                                        wraplength="4.5i")
        self.choosefile_lbl.grid(row=np.int(self.nfiles), column=1, columnspan=3)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def decrease(self):
        # Invoked when the decrease button is clicked.
        # It decrement the number of data files
        # It updates the label displaying the number of files.
        if (self.nfiles > 1):
            self.nfiles = self.nfiles - 1
            self.plan.configure(text="Compare " + str(self.nfiles) + " files")
        self.choosefile.destroy()
        self.choosefile_lbl.grid_forget()
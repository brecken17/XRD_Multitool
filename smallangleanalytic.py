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
matplotlib.use("TkAgg")


class tab():
    def __init__(self, tab):
        self.tab2 = tab
        # Screen title
        self.label = tk.Label(self.tab2, text="Utah - LIGO: Small Angle Analytic Simulation",
                      font=("Helvetica", 24)).grid(row=0, columnspan=5)
        # Spacer
        tk.Label(self.tab2,
         text='------------------------------------------------------------------------------------'
              '---------------------------------------------------------------').grid(row=1, columnspan=5)
        # Plot style
        LARGE_FONT = ("Verdana", 12)
        style.use("ggplot")
        # Establishes figure and subplot
        self.f = Figure(figsize=(4, 4), dpi=100)
        self.a = self.f.add_subplot(111)
        # creates and positions a canvas using the figure f
        self.canvas = FigureCanvasTkAgg(self.f, self.tab2)
        self.canvas.get_tk_widget().grid(row=2, columnspan=5)

        ###############    TOOLBAR    ###############
        self.toolbarFrame = tk.Frame(self.tab2)
        self.toolbarFrame.grid(row=3, columnspan=5)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbarFrame)
        # self.toolbar.update()
        # Spacer
        tk.Label(self.tab2,
         text='----------------------------------------------------------------------------------------'
              '-----------------------------------------------------------').grid(row=4, columnspan=5)
        # Choose file button
        self.choosefile = tk.Button(self.tab2, text="Choose data",
                            command=lambda: self.choosedatafile(self.choosefile_lbl
                                                                )).grid(row=5, column=1)
        # Data file label
        self.choosefile_lbl = tk.Label(self.tab2, text='-', font=("Arial Bold", 8), wraplength="4.5i")
        self.choosefile_lbl.grid(row=5, column=2, columnspan=3)
        # data file scaling
        self.datascalingentry = tk.Entry(self.tab2)
        self.datascalingentry.grid(row=5, column=4)
        self.datascalingentry.insert(0, '1.0')
        # Background data file label and button
        self.choosebackground = tk.Button(self.tab2, text="Background", command=lambda: self.choosedatafile
        (self.backgroundfile)).grid(row=6, column=1)
        self.backgroundfile = tk.Label(self.tab2, text='-', font=("ArialBold", 8), wraplength="4.5i")
        self.backgroundfile.grid(row=6, column=2, columnspan=3)
        # background file scaling
        self.backgroundscalingentry = tk.Entry(self.tab2)
        self.backgroundscalingentry.grid(row=6, column=4)
        self.backgroundscalingentry.insert(0, '1.0')
        # Entry box and label for thickness error
        self.thicknesserror_label = tk.Label(self.tab2, text="Thickness Error").grid(row=4, column=0)
        self.thicknesserror_entry = tk.Entry(self.tab2)
        self.thicknesserror_entry.grid(row=5, column=0)
        self.thicknesserror_entry.insert(0, '0.1')
        # Entry box and label for smoothing coefficient
        self.smoothing_label = tk.Label(self.tab2, text="Smoothing Coefficient").grid(row=6, column=0)
        self.smoothing_entry = tk.Entry(self.tab2)
        self.smoothing_entry.grid(row=7, column=0)
        self.smoothing_entry.insert(0, '0.05')  # inserts 0.1 into smoothing entry as default text
        # spacer
        tk.Label(self.tab2, text="").grid(row=7, column=3)
        # Inputs and labels
        # Entry box and label for itheta
        self.itheta_label = tk.Label(self.tab2, text="Initial Theta").grid(row=8, column=0)
        self.itheta_entry = tk.Entry(self.tab2)
        self.itheta_entry.grid(row=9, column=0)
        self.itheta_entry.insert(0, '0.2')  # inserts 0.2 into itheta entry as default text
        # Entry box and label for ftheta
        self.ftheta_label = tk.Label(self.tab2, text="Final Theta").grid(row=10, column=0)
        self.ftheta_entry = tk.Entry(self.tab2)
        self.ftheta_entry.grid(row=11, column=0)
        self.ftheta_entry.insert(0, '8')  # inserts 0.8 into itheta entry as default text
        # Entry box and label for theta stem
        self.thetastep_label = tk.Label(self.tab2, text="Step Size for Theta").grid(row=8, column=1)
        self.thetastep_entry = tk.Entry(self.tab2)
        self.thetastep_entry.grid(row=9, column=1)
        self.thetastep_entry.insert(0, '0.01')
        # Entry box and label for Scattering amplitude of material 2 in terms of material 1
        self.c1_label = tk.Label(self.tab2, text="Relative Scattering Amplitude").grid(row=10, column=1)
        self.c1_entry = tk.Entry(self.tab2)
        self.c1_entry.grid(row=11, column=1)
        self.c1_entry.insert(0, '0.5')
        # Entry box and label for number of layers per material
        self.layers_label = tk.Label(self.tab2, text="Number of Periods").grid(row=8, column=3)
        self.layers_entry = tk.Entry(self.tab2)
        self.layers_entry.grid(row=9, column=3)
        # LAbel and entry for Fraction of period taken up by material 1
        self.epsilon_label = tk.Label(self.tab2, text="Fraction of Material 1 in Period").grid(row=10, column=3)
        self.epsilon_entry = tk.Entry(self.tab2)
        self.epsilon_entry.grid(row=11, column=3)
        # label and entry for the Total thickness of the stack
        self.thickness_label = tk.Label(self.tab2, text="Thickness of Period (nm)").grid(row=8, column=4)
        self.thickness_entry = tk.Entry(self.tab2)
        self.thickness_entry.grid(row=9, column=4)
        # LAbel and entry for the scaling factor of the function
        self.scaling_label = tk.Label(self.tab2, text="Scaling Factor").grid(row=10, column=4)
        self.scaling_entry = tk.Entry(self.tab2)
        self.scaling_entry.grid(row=11, column=4)
        self.scaling_entry.insert(0, '100000000')
        # Spacer
        tk.Label(self.tab2,
         text='----------------------------------------------------------------------------------------------'
              '-----------------------------------------------------').grid(row=15, columnspan=5)
        # spacer
        tk.Label(self.tab2, text="").grid(row=16, column=3)
        # Update plot button
        self.update_plot_button = tk.Button(self.tab2, text="Plot", command=lambda: self.plot_update())\
            .grid(row=17, column=1)
        # spacer
        tk.Label(self.tab2, text="").grid(row=18, column=3)

        self.files = []

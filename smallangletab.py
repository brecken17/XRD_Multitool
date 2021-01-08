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
from SAmodel import *
from datahandling import *
matplotlib.use("TkAgg")


class tab():
    def __init__(self, tab):
        self.tab3 = tab
        self.label = tk.Label(self.tab3, text="Utah - LIGO: Small Angle Simulation",
                              font=("Helvetica", 24)).grid(row=0, columnspan=7)
        # Spacer
        tk.Label(self.tab3,
                 text='------------------------------------------------------------------------------------'
                      '---------------------------------------------------------------').grid(
            row=1, columnspan=5)
        # Plot style
        LARGE_FONT = ("Verdana", 12)
        style.use("ggplot")
        # Establishes figure and subplot
        self.f1 = Figure(figsize=(4, 4), dpi=100)
        self.a1 = self.f1.add_subplot(111)
        # creates and positions a canvas using the figure f
        self.canvas1 = FigureCanvasTkAgg(self.f1, self.tab3)
        self.canvas1.get_tk_widget().grid(row=2, columnspan=5)

        ###############    TOOLBAR    ###############
        self.toolbarFrame1 = tk.Frame(self.tab3)
        self.toolbarFrame1.grid(row=3, columnspan=5)
        self.toolbar1 = NavigationToolbar2Tk(self.canvas1, self.toolbarFrame1)
        # self.toolbar.update()
        # Spacer
        tk.Label(self.tab3,
                 text='----------------------------------------------------------------------------------------'
                      '-----------------------------------------------------------').grid(
            row=4, columnspan=5)
        # --------------------------------------------------------------------------------------------------------------
        # Choose file button
        self.choosefile1 = tk.Button(self.tab3, text="Choose data",
                                    command=lambda: choosedatafile(self.choosefile_lbl1, self.files)
                                     ).grid(row=5, column=0)
        # Data file label
        self.choosefile_lbl1 = tk.Label(self.tab3, text='-', font=("Arial Bold", 8), wraplength="4.5i")
        self.choosefile_lbl1.grid(row=5, column=1, columnspan=3)
        # --------------------------------------------------------------------------------------------------------------
        # data file scaling
        self.datascalingentry1 = tk.Entry(self.tab3)
        self.datascalingentry1.grid(row=5, column=4)
        self.datascalingentry1.insert(0, '1.0')
        # --------------------------------------------------------------------------------------------------------------
        # Background data file label and button
        self.choosebackground1 = tk.Button(self.tab3, text="Background", command=lambda: choosedatafile
        (self.backgroundfile1, self.files)).grid(row=6, column=0)
        self.backgroundfile1 = tk.Label(self.tab3, text='-', font=("ArialBold", 8), wraplength="4.5i")
        self.backgroundfile1.grid(row=6, column=1, columnspan=3)
        # --------------------------------------------------------------------------------------------------------------
        # background file scaling
        self.backgroundscalingentry1 = tk.Entry(self.tab3)
        self.backgroundscalingentry1.grid(row=6, column=4)
        self.backgroundscalingentry1.insert(0, '1.0')
        # --------------------------------------------------------------------------------------------------------------
        # Entry box and label for thickness error
        self.thicknesserror_label1 = tk.Label(self.tab3, text="Thickness Error").grid(row=12, column=1)
        self.thicknesserror_entry1 = tk.Entry(self.tab3)
        self.thicknesserror_entry1.grid(row=13, column=1)
        self.thicknesserror_entry1.insert(0, '0.1')
        # --------------------------------------------------------------------------------------------------------------
        # Entry box and label for smoothing coefficient
        self.smoothing_label1 = tk.Label(self.tab3, text="Smoothing Coefficient").grid(row=12, column=4)
        self.smoothing_entry1 = tk.Entry(self.tab3)
        self.smoothing_entry1.grid(row=13, column=4)
        self.smoothing_entry1.insert(0, '0.1')  # inserts 0.1 into smoothing entry as default text
        # spacer
        tk.Label(self.tab3, text="").grid(row=7, column=3)
        # --------------------------------------------------------------------------------------------------------------
        # Entry box and label for itheta
        self.itheta_label1 = tk.Label(self.tab3, text="Initial Theta").grid(row=8, column=0)
        self.itheta_entry1 = tk.Entry(self.tab3)
        self.itheta_entry1.grid(row=9, column=0)
        self.itheta_entry1.insert(0, '1')  # inserts 1 into itheta entry as default text
        # --------------------------------------------------------------------------------------------------------------
        # Entry box and label for ftheta
        self.ftheta_label1 = tk.Label(self.tab3, text="Final Theta").grid(row=10, column=0)
        self.ftheta_entry1 = tk.Entry(self.tab3)
        self.ftheta_entry1.grid(row=11, column=0)
        self.ftheta_entry1.insert(0, '15')  # inserts 15 into ftheta entry as default text
        # --------------------------------------------------------------------------------------------------------------
        # Entry box and label for theta stem
        self.thetastep_label1 = tk.Label(self.tab3, text="Step Size for Theta").grid(row=12, column=0)
        self.thetastep_entry1 = tk.Entry(self.tab3)
        self.thetastep_entry1.grid(row=13, column=0)
        self.thetastep_entry1.insert(0, '0.02')
        # --------------------------------------------------------------------------------------------------------------
        # Entry box and label for Scattering amplitude of material 2 in terms of material 1
        self.c1_label1 = tk.Label(self.tab3, text="Scattering Amplitude 1").grid(row=8, column=3)
        self.c1_entry1 = tk.Entry(self.tab3)
        self.c1_entry1.grid(row=9, column=3)
        self.c1_entry1.insert(0, '1.0')
        # --------------------------------------------------------------------------------------------------------------
        # Entry box and label for Scattering amplitude of material 2 in terms of material 1
        self.c2_label1 = tk.Label(self.tab3, text="Scattering Amplitude 2").grid(row=10, column=3)
        self.c2_entry1 = tk.Entry(self.tab3)
        self.c2_entry1.grid(row=11, column=3)
        self.c2_entry1.insert(0, '1.5')
        # --------------------------------------------------------------------------------------------------------------
        # Entry box and label for number of layers per material
        self.layers_label1 = tk.Label(self.tab3, text="Number of Periods").grid(row=8, column=4)
        self.layers_entry1 = tk.Entry(self.tab3)
        self.layers_entry1.grid(row=9, column=4)
        # --------------------------------------------------------------------------------------------------------------
        # label and entry for the Total thickness of the stack
        self.thickness2_label1 = tk.Label(self.tab3, text="Thickness of Material 2 (nm)").grid(row=10, column=1)
        self.thickness2_entry1 = tk.Entry(self.tab3)
        self.thickness2_entry1.grid(row=11, column=1)
        # --------------------------------------------------------------------------------------------------------------
        # label and entry for the Total thickness of the stack
        self.thickness1_label1 = tk.Label(self.tab3, text="Thickness of Material 1 (nm)").grid(row=8, column=1)
        self.thickness1_entry1 = tk.Entry(self.tab3)
        self.thickness1_entry1.grid(row=9, column=1)
        # --------------------------------------------------------------------------------------------------------------
        # Label and entry for the scaling factor of the function
        self.scale_label1 = tk.Label(self.tab3, text="Scaling Factor").grid(row=10, column=4)
        self.scale_entry1 = tk.Entry(self.tab3)
        self.scale_entry1.grid(row=11, column=4)
        self.scale_entry1.insert(0, '10')
        # --------------------------------------------------------------------------------------------------------------
        #Label and entry for the top level scattering amplitude
        self.topscat_label1 = tk.Label(self.tab3, text="Scattering Amplitude of Top Layer").grid(row=12, column=3)
        self.topscat_entry1 = tk.Entry(self.tab3)
        self.topscat_entry1.grid(row=13, column=3)
        self.topscat_entry1.insert(0, '1.0')
        # Spacer
        tk.Label(self.tab3,
                 text='----------------------------------------------------------------------------------------------'
                      '-----------------------------------------------------').grid(
            row=15, columnspan=5)
        # spacer
        tk.Label(self.tab3, text="").grid(row=16, column=3)
        # Update plot button
        self.update_plot_button = tk.Button(self.tab3, text="Plot", command=lambda: self.plot_update2()) \
            .grid(row=17, column=1)

        # spacer
        tk.Label(self.tab3, text="").grid(row=18, column=3)

        self.files = []
# ======================================================================================================================
# ======================================================================================================================
    def plot_update2(self):
        self.a1.clear()  # clears the plot so that we may plot a new data set
        lbd = 0.15406    # Sets the wavelength to 0.15406 nm
        xatt = 100000    # sets the attenuation value. This is arbitrary
        twot1 = []       # Creates an array for the two theta values
        xcnt1 = []       # Creates an array for the intensity values
        nbrsmpl = 40     # Sets the number of samples
    # ------------------------------------------------------------------------------------------------------------------
        # Creates data points from the XRD scan file of the front of the sample
        xf, yf = scan(self.smoothing_entry1.get(), self.files[0]).initialize_from_file()
        # Creates data points from the XRD scan file of the back of the sample
        xf0, yf0 = scan(self.smoothing_entry1.get(), self.files[1]).initialize_from_file()
        # Subtracts the intensity of the back of the data file from the intensity of the front of the data file
        ydif = np.array(yf) - np.array(yf0)
    # ------------------------------------------------------------------------------------------------------------------
        for k in range(0, nbrsmpl):
            print('Sample ' + str(k))
            # Build a sample
            sample = stack()
            for k in range(0, np.int(self.layers_entry1.get())):
                sample.add_layer(np.float(self.thickness1_entry1.get()) + np.random.uniform(-1 *
                                 np.float(self.thicknesserror_entry1.get()), np.float(self.thicknesserror_entry1.get()))
                                 , np.float(self.c1_entry1.get()))
                sample.add_layer(np.float(self.thickness2_entry1.get()) + np.random.uniform(-1 *
                                 np.float(self.thicknesserror_entry1.get()), np.float(self.thicknesserror_entry1.get()))
                                 , np.float(self.c2_entry1.get()))
            # Now add the substrate:
            sample.add_layer(0, np.float(self.topscat_entry1.get()))  # Thickness zero interpreted as infinite.

            # Calculate the model
            twot1, xcnt = sample.plot_xrdi(np.float(self.itheta_entry1.get()), np.float(self.ftheta_entry1.get()),
                                           np.float(self.thetastep_entry1.get()), lbd, xatt)
            del sample  # Delete the sample

            # Average the results
            if len(xcnt1) == 0:
                for l in range(0, len(xcnt)):
                    xcnt1.append(xcnt[l] / nbrsmpl)
            else:
                for l in range(0, len(xcnt1)):
                    xcnt1[l] = xcnt1[l] + xcnt[l] / nbrsmpl
    # ------------------------------------------------------------------------------------------------------------------
        # Creates a model of the substrate alone
        substrate = stack()
        substrate.add_layer(0, np.float(self.topscat_entry1.get()))  # Thickness zero interpreted as infinite
        # Calculates the model of the substrate alone
        twotb1, xcntb1 = substrate.plot_xrdi(np.float(self.itheta_entry1.get()), np.float(self.ftheta_entry1.get()),
                                             np.float(self.thetastep_entry1.get()), lbd, xatt)
        del substrate # Deletes the sample
    # ------------------------------------------------------------------------------------------------------------------
        BackgroundScale = np.array(yf0) / np.array(xcntb1[0:len(yf0)])
        # plots the difference between the front minus the back x-ray data as a function of two theta
        self.a1.plot(xf0, ydif, label='Scanned Data', linewidth=0, marker='.'
                    , color='steelblue')
        # Smooths the model data using a gauss function
        xg, yg = scan.initialize_from_gausssmoothing(twot1, xcnt1, float(self.smoothing_entry1.get()))
        # Plots the smoothed model data
        self.a1.plot(xg[0:len(yf0)], BackgroundScale * (np.float(self.scale_entry1.get()) * np.array(yg[0:len(yf0)])),
                     label='Simulated Data', color='indianred')
        # Sets the plot to be in log scale
        self.a1.set_yscale('log')
        # Sets a legend on the plot
        self.a1.legend()
        # Updates the canvas so the new data shows up
        self.canvas1.draw()
        self.tab3.update_idletasks()
        self.tab3.update()

# ======================================================================================================================
# ======================================================================================================================

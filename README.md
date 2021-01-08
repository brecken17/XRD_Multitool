# XRD_Multitool
Tool for the analysis of XRD data at the University of Utah and CalState LA

to run the tool, execute the file main.py using python3

# Tab 1

Do not use - work in progress
Will be a tool used for the characterization and analysis of crystallization peaks in XRD data

# Tab 2

Used for the analysis and modeling of small angle XRD data. A more thurough explaination of how to use the tool will be completed soon.

"Choose Data" Button - Selecting this button will open a file browser that will allow you to select the data file you wish to have plotted. The tool will only read the .txt data
                       output file from the Bruker D2 Phaser. The space where there is a "-" present will be replaced by the file name once the file is selected. Further to the
                       right is an input box with "1.0". This is the scaling factor applied to the selected data.

"Background" Button - Selecting this button will open a file browser that will allow you to select the background data file you wish to have subtracted from the data selected by
                      the "Choose Data" Button. The space where there is a "-" present will be replaced by the file name once the file is selected. Further to the right is an 
                      input box with "1.0". This is the scaling factor applied to the selected data.
                      
"Initial Theta" Field - The input here is for the initial two theta value of the model. Set to 1.0 degree two theta by default

"Final Theta" Field - The input here is for the final two theta value of the model. Set t0 15.0 degree two theta by default

"Step Size for Theta" Field - The input here is for the step size in theta, determining how many data points are in the model. Set to 0.02 degrees 2 theta by default.

"Thickness of Material 1" Field - The thickness of the 1st material in nanometers

"Thickness of Material 2" Field - The thickness of the 2nd material in nanometers

"Thickness Error" Field - The error in the thickness of the materials in nanometers. Each layer in the simulated sample varies by +/- a randomly selected value between 0 and the
                          input into the field.

"Scattering Amplitude 1" Field - Sets the scattering amplitude of the first material. This value is what differentiates the materials. Set to 1.5 by default.

"Scattering Amplitude 2" Field - Sets the scattering amplitude of the second material. This value is what differentiates the materials. Set to 1.0 by default.

"Scattering Amplitude of Substrate" Field - Sets the scattering amplitude of the substrate. Set to 1.0 by default.

"Number of Periods" Field - Sets the number of material pair layers. For instance if there are 124 layers of material 1, and 124 layers of material 2, in alternating layers,
                            then there are 124 material periods.

"Scaling Factor" Field - The modeled intensity is multiplied by this value.

"Smoothing Coefficient" Field - Chooses the standard deviation used in the gaussian smoothing that is applied to the modeled data.

"Plot" Button - Simulates and plots the model and plots the selected data set.


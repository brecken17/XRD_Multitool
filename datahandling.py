import numpy as np
from tkinter import filedialog

class scan:
    # This class collects the information of a scan whether the data
    # comes from a raw data file or from the processing of some raw data.
    def __init__(self, c, f):
        self.filename = f  # Name of file from which the data is to be read
        self.smtmplt = "-"  # Name of the file holding the smoothing template used
        self.subtract = "-"  # Name of the data file that was subtracted
        self.coef = c  # Normalization coefficient
        # self.label = t  # Label for legends
        self.x = []  # Two theta angle
        self.xerr = []  # Error on two theta angle
        self.y = []  # X-ray Count
        self.yerr = []  # Error on X-ray count.
        self.xmin = 0  # min x value
        self.xmax = 0  # max x value
        self.ymin = 0  # min y value
        self.ymax = 0  # max y value
        self.setxyminmax = False  # Becomes True when the min and max are set
        self.norm_fromx = 0  # Scan normalization left boundary
        self.norm_tox = 0  # Scan normalizatin right boundary
# ======================================================================================================================
# ======================================================================================================================
    def initialize_from_file(self):
        # This function open the file already specified as self.filename
        # It then reads the data to initialize the scan
        x = []
        y = []
        scanfile = open(self.filename, 'r')  # Open the data file
        lines = scanfile.readlines()  # Read the file in lines
        read = False  # The actual data has not been encountered yet
        for i in range(0, len(lines)):
            # Detect the end of the header
            if 'Angle,       PSD,' in lines[i]:
                read = True
                continue
            # If the end of the header has been encountered
            if (read):
                lines[i] = lines[i].replace(',', ' ')
                point = lines[i].split()  # Break the line in fields
                # Get x and y after removing the comas
                x.append(float(point[0].replace(',', '')))
                y.append(float(point[1].replace(',', '')))
        scanfile.close()  # Close the data file
        # Establishes the ranges for x and y
        # self.xyranges()
        # Set the errors in x and y
        # dx = 0.5 * (self.xmax - self.xmin) / len(x)
        # for k in range(0, len(x)):
        #    self.xerr.append(dx)
        #    self.yerr.append(np.sqrt(y))
        return x, y
# ======================================================================================================================
# ======================================================================================================================
    def initialize_from_gausssmoothing(rawx, rawy, sigma):
        # This function initialize a scan as the smoothing convolution
        # of the raw scan by a gauss function of standard deviation sigma.
        x = []
        y = []
        x.clear()
        y.clear()
        rawx = rawx
        rawy = rawy
        for k in range(0, len(rawx)):
            # The x entries of the smoothed scan are the same as the raw one
            x.append(rawx[k])
            # self.xerr.append(rawxerr[k])
            y.append(0.0)
            # yerr.append(0.0)
            total = 0.0
            # Convolution
            for j in range(0, len(rawx)):
                w = scan.normalgauss(rawx[j], x[k], sigma, 1.0)
                total = total + w
                y[k] = y[k] + rawy[j] * w
                # dy = raw.yerr[j] * w
                # self.yerr[k] = self.yerr[k] + dy * dy
            y[k] = y[k] / total
            # yerr[k] = np.sqrt(y[k]) / total
        # Establishes the ranges for x and y
        # self.xyranges()
        return x, y
        # Establishes the ranges for x and y
        # self.xyranges()
# ======================================================================================================================
# ======================================================================================================================
    def initialize_from_smoothing(self, raw, smtmplt):
        # This function initialises a scan with the data from the raw
        # scan smoothed with the data in the smoothing template smtmplt
        # Store the smoothing file name for refereence.
        self.smtmplt = smtmplt.filename
        # Set some values for the smoothed scan
        for k in range(0, len(raw.x)):
            self.x.append(raw.x[k])
            self.xerr.append(raw.xerr[k])
            self.y.append(raw.y[k] * smtmplt.c[0])
            total = smtmplt.c[0]
            dy = raw.yerr[k] * smtmplt.c[0]
            self.yerr.append(dy * dy)
            for j in range(1, len(smtmplt.c)):
                left = k - j
                if (left >= 0):
                    self.y[k] = self.y[k] + raw.y[left] * smtmplt.c[j]
                    dy = raw.yerr[left] * smtmplt.c[j]
                    self.yerr[k] = self.yerr[k] + dy * dy
                    total = total + smtmplt.c[j]
                right = k + j
                if (right < len(raw.x)):
                    self.y[k] = self.y[k] + raw.y[right] * smtmplt.c[j]
                    dy = raw.yerr[right] * smtmplt.c[j]
                    self.yerr[k] = self.yerr[k] + dy * dy
                    total = total + smtmplt.c[j]
            self.y[k] = self.y[k] / total
            self.yerr[k] = np.sqrt(self.yerr[k]) / total
        # Establishes the ranges for x and y
        self.xyranges()
# ======================================================================================================================
# ======================================================================================================================
    def normalgauss(x, x0, sigma, norm):
        # This function returns the evaluation in x of a Gauss function
        # centered in x0 with a standard deviation sigma and of norm norm
        if (sigma == 0): return 0
        g = np.exp(-(x - x0) * (x - x0) / (2 * sigma * sigma))
        g = g * norm / np.sqrt(2 * np.pi * sigma * sigma)
        return g
# ======================================================================================================================
# ======================================================================================================================
# Function to let us select data files via a button command
def choosedatafile(label, files):
    filename = filedialog.askopenfilename(initialdir=".", title="Select file", filetypes=(("text files", "*.txt"),
                                                                                          ("all files", "*.*")))
    files.append(filename)

    label.configure(text=filename[-50:-4])
# ======================================================================================================================
# ======================================================================================================================
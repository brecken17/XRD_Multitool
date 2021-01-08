import numpy as np
import matplotlib.pyplot as plt

# import random
j = complex(0, 1)
pi = np.pi
rad = 180.0 / pi


# ======================================================================================================================
# ======================================================================================================================
class layerc:
    def __init__(self, t, s, d):
        self.thick = t  # Thickness of layer
        # Note: a zero thickness will be interpreted at infinite.
        self.scata = s  # Scattering amplitude coefficient in layer
        self.depth = d  # Depth of the top of the layer

    # ------------------------------------------------------------------------------------------------------------------
    def print(self):
        # This function prints out layer information
        print(f'Depth: {self.depth:5}nm,', end='')
        print(f'  Thickness: {self.thick:5}nm,', end='')
        print(f' Scattering: {self.scata:5}.')

    # ------------------------------------------------------------------------------------------------------------------
    def amplay(self, theta, k):
        # Calculate the complex amplitude contribution from the
        # layer for an angle theta and a complex wavenumber k
        if self.thick == 0:  # Contribution from the substrate
            a = -self.scata * np.exp(k * self.depth)
        else:
            a = self.scata * (np.exp(k * self.thick) - 1.0) * np.exp(k * self.depth)
        return a

# ======================================================================================================================
# ======================================================================================================================
class stack:
    def __init__(self):
        self.nlayr = 0  # Number of layers
        self.layer = []

    # ------------------------------------------------------------------------------------------------------------------
    def add_layer(self, thick, scata):
        # This function can be used to add a layer of thickness thick
        # and scattering amplitude coef scata.
        # If the last layer is of infinite thickness, we can not add
        if self.nlayr > 0:
            if self.layer[-1].thick == 0:
                fatalerror("Adding layer below substrate in add_layer()")
        self.nlayr = self.nlayr + 1  # Increment the number of layers
        depth = 0  # Calculate the depth of top of the new layer
        if self.nlayr > 1:
            depth = self.layer[-1].depth + self.layer[-1].thick
        l = layerc(thick, scata, depth)  # Creat the layer
        self.layer.append(l)  # Add the layer to the stack

    # ------------------------------------------------------------------------------------------------------------------
    def print(self):
        # Prints the stack
        print('-------------------------------------------')
        print(str(self.nlayr) + ' layers;')
        for k in range(0, self.nlayr):
            print('  {}:   '.format(k + 1), end='', flush=True)
            self.layer[k].print()
        print('-------------------------------------------')

    # ------------------------------------------------------------------------------------------------------------------
    def kappa(self, theta, lbd, xatt):
        # Calculates the complex slanted wave number kappa. The
        # imaginary part is twice the wave number and the real part
        # corresponds to twice the attenuation.
        if lbd < 0:
            fatalerror("lbd out of range in kappa(theta, lbd, xatt)")
        if xatt < 0:
            fatalerror("xatt out of range in kappa(theta, lbd, xatt)")
        sint = np.sin(theta)
        if sint == 0:
            fatalerror("theta out of range in kappa(theta, lbd, xatt)")
        k = 4.0 * pi * j * sint / lbd
        k = k - 2.0 / (sint * xatt)
        return k

    # ------------------------------------------------------------------------------------------------------------------
    def xrdi(self, twot, lbd, xatt):
        # Calculate the XRD intensity for the stack as a
        # function of the two-theta angle twot for the X-ray
        # wavelength lbd and attenuation xatt.
        theta = 0.5 * twot
        k = self.kappa(theta, lbd, xatt)
        if np.abs(k) == 0:
            fatalerror('Wave number k out of range in xrdi(sample,twot,lbd,xatt')
        a = 0  # amplitude
        for m in range(0, self.nlayr):
            a = a + self.layer[m].amplay(theta, k)
        a = a / k

        i = a * a.conjugate()
        return i.real
    # ------------------------------------------------------
    def plot_xrdi(self, tmin, tmax, tstp, lbd, xatt):
        # This function calculates the model for angles ranging
        # from tmin to tmax in tstp steps for an X-ray wave length
        # lbd and an attenuation xatt.
        tmin = tmin / rad
        tmax = tmax / rad
        tstp = tstp / rad

        x = []  # Array for the values of two theta
        y = []  # Array for the model values
        for t in np.arange(tmin, tmax, tstp):
            x.append(t * rad)
            i = self.xrdi(t, lbd, xatt)
            y.append(i)
        return x, y
# ======================================================================================================================
# ======================================================================================================================
def fatalerror(msg):
    # This function is used to print an error message and
    # terminate the execution
    print(msg)
    print("Program terminating now")
    exit()


# ======================================================================================================================
# ======================================================================================================================

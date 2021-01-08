class fitting:
    def __init__(self):

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
    def getintegdone():
        # This function sums up the raw data count between the
        # boundaries entered by the user. The result is printed
        # on the terminal.

        # Get the left and right boundaries
        xleft = float(xleftntries.get())
        xright = float(xrightntries.get())
        # Deals with possible misordering of the boundaries so right>left
        if (xleft > xright):
            dummy = xleft
            xleft = xright
            xright = dummy

        sum = []
        for k in range(0, len(r)):  # loops on all the raw data scans
            sum.append(0)  # Initialises the sum
            for j in range(0, len(r[k].x)):
                if (r[k].x[j] > xleft and r[k].x[j] < xright):
                    sum[k] = sum[k] + r[k].y[j]  # update the sum in the chosen interval

        print("=========================================================")
        for k in range(0, len(r)):  # loops on all the raw data scans
            ratio = sum[k] * 1.0 / sum[len(r) - 1]
            print("%s: %f between % f and % f. Ratio: % f" % (r[k].label, sum[k], xleft, xright, ratio))
        print("=========================================================")
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
    def getfitdone():
        # This function fits a gauss function added with a first degree
        # polynomial to the data between the selected boundaries.

        # Get the left and right boundaries
        xleft = float(xleftntries.get())
        xright = float(xrightntries.get())
        # Deals with possible misordering of the boundaries so right>left
        if (xleft > xright):
            dummy = xleft
            xleft = xright
            xright = dummy

        scount = 0  # Number of scans to be fitted
        if (smooth == False):
            scount = len(r)
        else:
            scount = len(s)
        for k in range(0, scount):  # For each scan
            xf = []  # Array for 2theta
            yf = []  # Array for counts
            for j in range(0, len(r[k].x)):  # Get the data from the selected range
                if (r[k].x[j] > xleft and r[k].x[j] < xright):
                    if (smooth == False):
                        xf.append(r[k].x[j])
                        yf.append(r[k].y[j])
                    else:
                        xf.append(s[k].x[j])
                        yf.append(s[k].y[j])

            if (len(xf) < 7):  # If there are not enought samples
                print("%s: Fit abborted. Insufficient selected data." % r[k].label)
                continue
            # The data is shifted so the first point is in (0,0)
            # At the same time the min and max counts are indentified
            xref = xf[0]
            yref = yf[0]
            ymin = 0
            ymax = 0
            for j in range(0, len(xf)):
                xf[j] = xf[j] - xref
                yf[j] = yf[j] - yref
                if (yf[j] > ymax): ymax = yf[j]
                if (yf[j] < ymin): ymin = yf[j]
            yrange = ymax - ymin  # Counts range
            xmax = xf[-1]
            xstep = xmax / (len(xf) - 1)  # This is the difference between successive xf values
            # Both 2theta and counts are rescales to the interval [0,1]
            for j in range(0, len(xf)):
                yf[j] = yf[j] / yrange
                xf[j] = xf[j] / xmax
            # Proceed to the fit
            popt, pcov = curve_fit(p1gaussf, xf, yf,
                               bounds=([-10, -10, .5, 0, 0], [10, 10, xf[-1], xf[-1], 1000]))
            # Plot the fitted function on the scan graph
            px = []
            py = []
            npoints = 50
            for j in range(0, npoints):
                sx = float(j) / npoints
                px.append(xref + sx * xmax)
                f = p1gaussf(sx, *popt)
                py.append(yref + yrange * f)
                grph.plot(px, py, 'red',
                      linewidth=3, linestyle='dotted')
            canvas.draw()

            # Printout the fitted parameters
            print("========FIT for ", r[k].label, " ===================")
            print("a=%f+/-%g"
              % (yrange * popt[0] / xmax, yrange * np.sqrt(pcov[0][0]) / xmax))
            print("b=%f+/-%g"
              % (yref + yrange * popt[1], yrange * np.sqrt(pcov[1][1])))
            print("x0=%f+/-%g"
              % (xref + xmax * popt[2], xmax * np.sqrt(pcov[2][2])))
            print("sigma=%f+/-%g"
              % (xmax * popt[3], xmax * np.sqrt(pcov[3][3])))
            print("norm=%f+/-%g"
              % (xmax * yrange * popt[4] / xstep, xmax * yrange * np.sqrt(pcov[4][4]) / xstep))
            print("===========================================")
            print(xmax)
            print(xstep)
            print(len(xf))

    def getfitdone2():
        # This function fits three gauss functions one added with a first degree to fit to two narrow peaks and
        # one broad peak underneath
        # polynomial to the data between the selected boundaries.

        # obtaining fit parameters obtained from the given values on the run analysis menu
        peakonebounds = peakone
        peakonebounds = eval(peakonebounds.split()[0])
        peakonebounds = np.array(peakonebounds)
        peaktwobounds = peaktwo
        peaktwobounds = eval(peaktwobounds.split()[0])
        peaktwobounds = np.array(peaktwobounds)
        peakbroadbounds = peakbroad
        peakbroadbounds = eval(peakbroadbounds.split()[0])
        peakbroadbounds = np.array(peakbroadbounds)

        # Get the left and right boundaries
        xleft = float(xleftntries.get())
        xright = float(xrightntries.get())
        # Deals with possible misordering of the boundaries so right>left
        if (xleft > xright):
            dummy = xleft
            xleft = xright
            xright = dummy

        scount = 0  # Number of scans to be fitted
        if (smooth == False):
            scount = len(r)
        else:
            scount = len(s)
        for k in range(0, scount):  # For each scan
            xf = []  # Array for 2theta
            yf = []  # Array for counts
            for j in range(0, len(r[k].x)):  # Get the data from the selected range
                if (r[k].x[j] > xleft and r[k].x[j] < xright):
                    if (smooth == False):
                        xf.append(r[k].x[j])
                        yf.append(r[k].y[j])
                    else:
                        xf.append(s[k].x[j])
                        yf.append(s[k].y[j])

            if (len(xf) < 7):  # If there are not enought samples
                print("%s: Fit abborted. Insufficient selected data." % r[k].label)
                continue

            xrange = xf[-1] - xf[0]  # This variable contains the difference of the starting x value and the ending x value
            xstep = xrange / (len(xf) - 1)  # This is the difference between successive xf values

            guess = [(peakonebounds[0] + peakonebounds[1]) / 2,
                 (peakonebounds[2] + peakonebounds[3]) / 2, 0 + peakonebounds[4],
                 (peaktwobounds[0] + peaktwobounds[1]) / 2,
                 (peaktwobounds[2] + peaktwobounds[3]) / 2, 0 + peaktwobounds[4],
                 (peakbroadbounds[0] + peakbroadbounds[1]) / 2,
                 (peakbroadbounds[2] + peakbroadbounds[3]) / 2, 0 + peakbroadbounds[4], 8.70,
                 0]  # The fit will start searching for values near the guess values
            # Proceed to the fit
            popt, pcov = curve_fit(threepeakgauss, xf, yf, p0=guess,
                               bounds=([peakonebounds[0], peakonebounds[2], peakonebounds[4],
                                        peaktwobounds[0], peaktwobounds[2], peaktwobounds[4],
                                        peakbroadbounds[0], peakbroadbounds[2], peakbroadbounds[4], -500, -100],
                                       [peakonebounds[1], peakonebounds[3], peakonebounds[5],
                                        peaktwobounds[1], peaktwobounds[3], peaktwobounds[5],
                                        peakbroadbounds[1], peakbroadbounds[3], peakbroadbounds[5], 500,
                                        100]))  # setting up bounds obtained from parameters
            # Plot the fitted function on the scan graph
            fit = threepeakgauss(xf, *popt)

            grph.plot(xf, fit, 'red',
                  linewidth=3, linestyle='dotted')
            canvas.draw()

            # Printout the fitted parameters
            print("========FIT for ", r[k].label, " ===================")
            print("===========================================")
            print("x10=%f+/-%g" % (popt[0], np.sqrt(pcov[0][0])))
            print("sigma1=%f+/-%g" % (popt[1], np.sqrt(pcov[1][1])))
            print("CrystalSize1=%f+/-%g" % (3.3207 / (math.cos(math.radians(popt[0])) * popt[1]),
                                        (3.3207 / (math.cos(math.radians(popt[0])) * popt[1] * popt[1]) * np.sqrt(
                                            pcov[1][1]))))
            print("norm1=%f+/-%g" % (popt[2] / xstep, np.sqrt(pcov[2][2]) / xstep))
            print("===========================================")
            print("x20=%f+/-%g" % (popt[3], np.sqrt(pcov[3][3])))
            print("sigma2=%f+/-%g" % (popt[4], np.sqrt(pcov[4][4])))
            print("CrystalSize2=%f+/-%g" % (3.3207 / (math.cos(math.radians(popt[3])) * popt[4]),
                                        (3.3207 / (math.cos(math.radians(popt[3])) * popt[4] * popt[4]) * np.sqrt(
                                            pcov[4][4]))))
            print("norm2=%f+/-%g" % (popt[5] / xstep, np.sqrt(pcov[5][5]) / xstep))
            print("===========================================")
            print("x30=%f+/-%g" % (popt[6], np.sqrt(pcov[6][6])))
            print("sigma3=%f+/-%g" % (popt[7], np.sqrt(pcov[7][7])))
            print("CrystalSize3=%f+/-%g" % (3.3207 / (math.cos(math.radians(popt[6])) * popt[7]),
                                        (3.3207 / (math.cos(math.radians(popt[6])) * popt[7] * popt[7]) * np.sqrt(
                                            pcov[7][7]))))
            print("norm3=%f+/-%g" % (popt[8] / xstep, np.sqrt(pcov[8][8]) / xstep))
            print("===========================================")
            print("===========================================")
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
    def getfitdone3():
        # This function fits four gauss functions one added with a first degree to fit to two narrow peaks and
        # two broad peak underneath
        # polynomial to the data between the selected boundaries.

        # obtaining fit parameters obtained from the given values on the run analysis menu
        peakonebounds = peakone
        peakonebounds = eval(peakonebounds.split()[0])
        peakonebounds = np.array(peakonebounds)
        peaktwobounds = peaktwo
        peaktwobounds = eval(peaktwobounds.split()[0])
        peaktwobounds = np.array(peaktwobounds)
        peakbroadbounds = peakbroad
        peakbroadbounds = eval(peakbroadbounds.split()[0])
        peakbroadbounds = np.array(peakbroadbounds)
        peaktwobroadbounds = peaktwobroad
        peaktwobroadbounds = eval(peaktwobroadbounds.split()[0])
        peaktwobroadbounds = np.array(peaktwobroadbounds)

        # Get the left and right boundaries
        xleft = float(xleftntries.get())
        xright = float(xrightntries.get())
        # Deals with possible misordering of the boundaries so right>left
        if (xleft > xright):
            dummy = xleft
            xleft = xright
            xright = dummy

        scount = 0  # Number of scans to be fitted
        if (smooth == False):
            scount = len(r)
        else:
            scount = len(s)
        for k in range(0, scount):  # For each scan
            xf = []  # Array for 2theta
            yf = []  # Array for counts
            for j in range(0, len(r[k].x)):  # Get the data from the selected range
                if (r[k].x[j] > xleft and r[k].x[j] < xright):
                    if (smooth == False):
                        xf.append(r[k].x[j])
                        yf.append(r[k].y[j])
                    else:
                        xf.append(s[k].x[j])
                        yf.append(s[k].y[j])

            if (len(xf) < 7):  # If there are not enought samples
                print("%s: Fit abborted. Insufficient selected data." % r[k].label)
                continue

            xrange = xf[-1] - xf[0]
            # This variable contains the difference of the starting x value and the ending x value
            xstep = xrange / (len(xf) - 1)  # This is the difference between successive xf values

            guess = [(peakonebounds[0] + peakonebounds[1]) / 2,
                 (peakonebounds[2] + peakonebounds[3]) / 2, 0 + peakonebounds[4],
                 (peaktwobounds[0] + peaktwobounds[1]) / 2,
                 (peaktwobounds[2] + peaktwobounds[3]) / 2, 0 + peaktwobounds[4],
                 (peakbroadbounds[0] + peakbroadbounds[1]) / 2,
                 (peakbroadbounds[2] + peakbroadbounds[3]) / 2, 0 + peakbroadbounds[4],
                 (peaktwobroadbounds[0] + peaktwobroadbounds[1]) / 2,
                 (peaktwobroadbounds[2] + peaktwobroadbounds[3]) / 2, 0 + peaktwobroadbounds[4],
                 8.70, 0]
            # The fit will start searching for values near the guess values
            # Proceed to the fit
            popt, pcov = curve_fit(fourpeakgauss, xf, yf, p0=guess,
                               bounds=([peakonebounds[0], peakonebounds[2], peakonebounds[4],
                                        peaktwobounds[0], peaktwobounds[2], peaktwobounds[4],
                                        peakbroadbounds[0], peakbroadbounds[2], peakbroadbounds[4],
                                        peaktwobroadbounds[0], peaktwobroadbounds[2], peaktwobroadbounds[4], -500,
                                        -100],
                                       [peakonebounds[1], peakonebounds[3], peakonebounds[5],
                                        peaktwobounds[1], peaktwobounds[3], peaktwobounds[5],
                                        peakbroadbounds[1], peakbroadbounds[3], peakbroadbounds[5],
                                        peaktwobroadbounds[1], peaktwobroadbounds[3], peaktwobroadbounds[5], 500,
                                        100]))  # setting up bounds obtained from parameters
            # Plot the fitted function on the scan graph
            fit = fourpeakgauss(xf, *popt)

            grph.plot(xf, fit, 'red', linewidth=3, linestyle='dotted')
            canvas.draw()

            # Printout the fitted parameters
            print("========FIT for ", r[k].label, " ===================")
            print("===========================================")
            print("x10=%f+/-%g" % (popt[0], np.sqrt(pcov[0][0])))
            print("sigma1=%f+/-%g" % (popt[1], np.sqrt(pcov[1][1])))
            print("CrystalSize1=%f+/-%g" % (3.3207 / (math.cos(math.radians(popt[0])) * popt[1]),
                                        (3.3207 / (math.cos(math.radians(popt[0])) * popt[1] * popt[1]) * np.sqrt(
                                            pcov[1][1]))))
            print("norm1=%f+/-%g" % (popt[2] / xstep, np.sqrt(pcov[2][2]) / xstep))
            print("===========================================")
            print("x20=%f+/-%g" % (popt[3], np.sqrt(pcov[3][3])))
            print("sigma2=%f+/-%g" % (popt[4], np.sqrt(pcov[4][4])))
            print("CrystalSize2=%f+/-%g" % (3.3207 / (math.cos(math.radians(popt[3])) * popt[4]),
                                        (3.3207 / (math.cos(math.radians(popt[3])) * popt[4] * popt[4]) * np.sqrt(
                                            pcov[4][4]))))
            print("norm2=%f+/-%g" % (popt[5] / xstep, np.sqrt(pcov[5][5]) / xstep))
            print("===========================================")
            print("x30=%f+/-%g" % (popt[6], np.sqrt(pcov[6][6])))
            print("sigma3=%f+/-%g" % (popt[7], np.sqrt(pcov[7][7])))
            print("CrystalSize3=%f+/-%g" % (3.3207 / (math.cos(math.radians(popt[6])) * popt[7]),
                                        (3.3207 / (math.cos(math.radians(popt[6])) * popt[7] * popt[7]) * np.sqrt(
                                            pcov[7][7]))))
            print("norm3=%f+/-%g" % (popt[8] / xstep, np.sqrt(pcov[8][8]) / xstep))
            print("===========================================")
            print("x40=%f+/-%g" % (popt[9], np.sqrt(pcov[9][9])))
            print("sigma4=%f+/-%g" % (popt[10], np.sqrt(pcov[10][10])))
            print("CrystalSize4=%f+/-%g" % (3.3207 / (math.cos(math.radians(popt[9])) * popt[10]),
                                        (3.3207 / (math.cos(math.radians(popt[9])) * popt[10] * popt[10]) * np.sqrt(
                                            pcov[10][10]))))
            print("norm4=%f+/-%g" % (popt[11] / xstep, np.sqrt(pcov[11][11]) / xstep))
            print("===========================================")
            print("===========================================")
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

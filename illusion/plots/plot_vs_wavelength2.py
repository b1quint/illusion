#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Plot Intensity x Gap for the central pixel of a Fabry-Perot using Illusion.
"""

import illusion
import matplotlib.pyplot as pyplot

myCCD = illusion.fpdata.Detector(1, 1, 150000, 0.16)
myFP = illusion.fpdata.FabryPerot(0.550, 2000, 25, 350 * 1e-3)

myFP.g_step = myFP.g_step / 500
print myFP.g_start

myFP.raw_cube(myCCD, source_wavelength=0.550, source_intensity=1000.)
oneData = myCCD.data[:,0,0].copy()
pyplot.plot(oneData, "k-")

myFP.raw_cube(myCCD, source_wavelength=0.551, source_intensity=1000.)
oneData = myCCD.data[:,0,0].copy()
pyplot.plot(oneData, "k--")

myFP.raw_cube(myCCD, source_wavelength=0.602, source_intensity=1000.)
oneData = myCCD.data[:,0,0].copy()
pyplot.plot(oneData, "r-")

pyplot.ylim(-10, 1050)
#pyplot.title("Periodicidade de um Fabry-Perot.")
pyplot.xlabel("$\delta(d)$", fontsize=20)
pyplot.ylabel("$I^{(t)}/I^{(i)}$", fontsize=20, rotation='horizontal')
pyplot.xticks(range(0))
pyplot.yticks(range(0))

x, y, dx, dy = 35000, 500, 15000-4000, 0
pyplot.arrow(x, y, dx, dy, head_width=50, head_length=2500, width=15, fc="k", head_starts_at_zero=True)
x, y, dx, dy = 40000, 500, -dx, dy
pyplot.arrow(x, y, dx, dy, head_width=50, head_length=2500, width=15, fc="k", head_starts_at_zero=True)

pyplot.text(33000, 525, "$FSR_d$", fontsize=24)

pyplot.annotate('$\lambda_0$', xy=(100000, 600),  xycoords='data',
                xytext=(40, -50), textcoords='offset points',
                size=16,
                #bbox=dict(boxstyle="round", fc="0.8"),
                arrowprops=dict(arrowstyle="simple",
                                fc="0.2", ec="none",
                                #patchB=el,
                                connectionstyle="arc3,rad=0.3"),)

pyplot.annotate('$\lambda_0 + \sigma$', xy=(103500, 750),  xycoords='data',
                xytext=(30, -50), textcoords='offset points',
                size=16,
                #bbox=dict(boxstyle="round", fc="0.8"),
                arrowprops=dict(arrowstyle="simple",
                                fc="0.4", ec="none",
                                #patchB=el,
                                connectionstyle="arc3,rad=0.3"),)

pyplot.annotate('$\lambda$', xy=(107000, 900),  xycoords='data',
                xytext=(30, -50), textcoords='offset points',
                size=16,
                #bbox=dict(boxstyle="round", fc="0.8"),
                arrowprops=dict(arrowstyle="simple",
                                fc="#FFAAAA", ec="none",
                                #patchB=el,
                                connectionstyle="arc3,rad=0.3"),)

pyplot.show()

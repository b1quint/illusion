#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Plot Intensity x Gap for the central pixel of a Fabry-Perot using Illusion.
"""

from numpy import arange
import illusion
import matplotlib.pyplot as pyplot
import sys

myCCD = illusion.fpdata.Detector(1, 1, 100000, 0.16)
myFP = illusion.fpdata.FabryPerot(0.550, 2000, 25, 350 * 1e-3)

myFP.g_step = myFP.g_step / 500
print myFP.g_start

myFP.raw_cube(myCCD, source_wavelength=0.550, source_intensity=1000.)
oneData = myCCD.data[:,0,0].copy()
pyplot.plot(oneData, "k-")

if len(sys.argv) > 1:
    if sys.argv[1] == '2':
        myFP.raw_cube(myCCD, source_wavelength=0.551, source_intensity=1000.)
        oneData = myCCD.data[:,0,0].copy()
        pyplot.plot(oneData, "k--")
    if sys.argv[1] == '3':
        
        myFP.raw_cube(myCCD, source_wavelength=0.551, source_intensity=1000.)
        oneData = myCCD.data[:,0,0].copy()
        pyplot.plot(oneData, "k--")
        
        myFP.raw_cube(myCCD, source_wavelength=0.552, source_intensity=1000.)
        oneData = myCCD.data[:,0,0].copy()
        pyplot.plot(oneData, "k:")

pyplot.ylim(-10, 1050)
#pyplot.title("Periodicidade de um Fabry-Perot.")
pyplot.title("Periodicity in a Fabry-Perot.")
pyplot.xlabel("$\delta(d)$", fontsize=20)
pyplot.ylabel("$I^{(t)}/I^{(i)}$", fontsize=20, rotation='horizontal')
pyplot.xticks(25000*arange(3)+25000,('$2\pi(m-2)$', '$2\pi(m-1)$', '$2\pi m$', '$2\pi(m+1)$', '2\pi(m+2)$'))
pyplot.yticks(range(0))

x, y, dx, dy = 35000, 500, 15000-4000, 0
pyplot.arrow(x, y, dx, dy, head_width=50, head_length=2500, width=15, fc="k", head_starts_at_zero=True)
x, y, dx, dy = 40000, 500, -dx, dy
pyplot.arrow(x, y, dx, dy, head_width=50, head_length=2500, width=15, fc="k", head_starts_at_zero=True)

pyplot.text(33000, 525, "$FSR_d$", fontsize=24)

pyplot.annotate('$\lambda_0$', xy=(50000, 600),  xycoords='data',
                xytext=(40, -50), textcoords='offset points',
                size=16,
                #bbox=dict(boxstyle="round", fc="0.8"),
                arrowprops=dict(arrowstyle="simple",
                                fc="0.2", ec="none",
                                #patchB=el,
                                connectionstyle="arc3,rad=0.3"),)
if len(sys.argv) > 1:
    if sys.argv[1] == '2':
        pyplot.annotate('$\lambda_0 + \sigma$', xy=(53000, 750),  xycoords='data',
                        xytext=(30, -50), textcoords='offset points',
                        size=16,
                        #bbox=dict(boxstyle="round", fc="0.8"),
                        arrowprops=dict(arrowstyle="simple",
                                        fc="0.4", ec="none",
                                        #patchB=el,
                                        connectionstyle="arc3,rad=0.3"),)
    if sys.argv[1] == '3':
        pyplot.annotate('$\lambda_0 + \sigma$', xy=(53000, 750),  xycoords='data',
                        xytext=(30, -50), textcoords='offset points',
                        size=16,
                        #bbox=dict(boxstyle="round", fc="0.8"),
                        arrowprops=dict(arrowstyle="simple",
                                        fc="0.4", ec="none",
                                        #patchB=el,
                                        connectionstyle="arc3,rad=0.3"),)        

        pyplot.annotate('$\lambda_0 + 2\sigma$', xy=(57000, 900),  xycoords='data',
                        xytext=(30, -50), textcoords='offset points',
                        size=16,
                        #bbox=dict(boxstyle="round", fc="0.8"),
                        arrowprops=dict(arrowstyle="simple",
                                        fc="0.6", ec="none",
                                        #patchB=el,
                                        connectionstyle="arc3,rad=0.3"),)

pyplot.show()

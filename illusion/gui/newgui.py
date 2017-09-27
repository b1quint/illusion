"""#
#=============================================================================
#  __   __
# (  \,/  )
#  \_ | _/      Butterfly Software System
#  (_/ \_)
#
#
# Illusion Graphical User Interface - v0.1
# by Bruno Quint - Jan 15, 2010
#
#-----------------------------------------------------------------------------
# Illusion GUI written in TkInter that writes a "conf" file and run the
# Illusion Engine.
"""

import subgui as sgui
import subprocess as sproc
import Tkinter as tk

__author__ = "Bruno Quint"
__version__ = "v0.2"
__date__ = "2010.02.22"

##============================================================================
## CLASS IllusionGUI
class IllusionGUI:
    """
    Illusion GUI is a graphical interface to run the Illusion Engine. All the
    text field are parsed to a config file that will be used as an input
    for Illusion Engine.
    """

    ##------------------------------------------------------------------------
    ## METHOD __init__
    def __init__(self, master):
        """
        The graphical interface main constructor. It automatically loads
        all the widgets that is contained in the screen by calling a method
        for each child frame shown in the interface.

        @param master: parent widget (e.g. a Tkinter.Frame)
        """
        self.setMainFrame(master)
        self.setFPFrame(master)
        self.setCCDFrame(master)
        self.setCubeTypeFrame(master)
        self.setFilesFrame(master)
        self.setButtonsFrame(master)
        self.setStandardValues()

    ##------------------------------------------------------------------------
    ## METHOD setMainFrame
    def setMainFrame(self, master):
        """
        Define the parent window's parameters making it suitable to receive
        the child frames.

        @param master: parent widget (e.g. a Tkinter.Frame)
        """
        master.title("Illusion " + __version__ + " - Data Cube Synthesizer")
        master.minsize(800,300)
        master.resizable(0,0)

    ##------------------------------------------------------------------------
    ## METHOD setFPFrame
    def setFPFrame(self,master):
        """
        This frame will contain all the information regarding to the
        Fabry-Perot itself that will be parsed in the config file.
        Some parameters regarding the optics and other options are also
        included here.

        @param master: parent widget (e.g. a Tkinter.Frame)
        """
        frameFP = tk.Frame(master)
        self.centralWavelength	= sgui.Input(frameFP,
                                t1="Central wavelength: ",t2=" nm")
        self.spectralResolution	= sgui.Input(frameFP,t1="Spectral resolution: ")
        self.finesse            = sgui.Input(frameFP,t1="Finesse: ")
        self.extrapolate        = sgui.Input(frameFP,t1="Extrapolate: ", t2="%")
        self.focalLength        = sgui.Input(frameFP,t1="Focal length: ",t2=" mm")
        self.noisevar = tk.IntVar()
        self.noise 	  = tk.Checkbutton(frameFP,
                        text="Add poisson noise",variable=self.noisevar)

        frameFP.grid(row=0,column=0,sticky=tk.N)
        frameFP.config(borderwidth=1, relief=tk.RIDGE)
        frameFP.config(padx=10,pady=10)

        self.centralWavelength.label1.grid(row=0,column=0,sticky=tk.W)
        self.centralWavelength.label2.grid(row=0,column=2,sticky=tk.W)
        self.centralWavelength.tBox.grid(row=0,column=1,sticky=tk.W)

        self.spectralResolution.label1.grid(row=1,column=0,sticky=tk.W)
        self.spectralResolution.tBox.grid(row=1,column=1,sticky=tk.W)

        self.finesse.label1.grid(row=2,column=0,sticky=tk.W)
        self.finesse.tBox.grid(row=2,column=1,sticky=tk.W)

        self.extrapolate.label1.grid(row=3,column=0,sticky=tk.W)
        self.extrapolate.label2.grid(row=3,column=2,sticky=tk.W)
        self.extrapolate.tBox.grid(row=3,column=1,sticky=tk.W)

        self.focalLength.label1.grid(row=4,column=0,sticky=tk.W)
        self.focalLength.label2.grid(row=4,column=2,sticky=tk.W)
        self.focalLength.tBox.grid(row=4,column=1,sticky=tk.W)

        self.noise.grid(row=5,column=1,sticky=tk.E)

        self.centralWavelength.tBox.configure(justify=tk.RIGHT)
        self.spectralResolution.tBox.configure(justify=tk.RIGHT)
        self.finesse.tBox.configure(justify=tk.RIGHT)
        self.extrapolate.tBox.configure(justify=tk.RIGHT)
        self.focalLength.tBox.configure(justify=tk.RIGHT)

    ##------------------------------------------------------------------------
    ## METHOD setCCDFrame
    def setCCDFrame(self, master):
        """
        This frame will contain all the information regarding to the
        Detector itself that will be parsed in the config file.

        @param master: parent widget (e.g. a Tkinter.Frame)
        """
        frameCCD 	= tk.Frame(master)
        self.ccdWidth	= sgui.Input(frameCCD,t1="Detector's width: ",t2=" pixels")
        self.ccdHeight	= sgui.Input(frameCCD,t1="Detector's height: ",t2=" pixels")
        self.pixelSize	= sgui.Input(frameCCD,t1="Pixel's size: ", t2=" microns")
        self.binning	= sgui.Input(frameCCD,t1="Binning: ")

        frameCCD.grid(row=0,column=1,sticky=tk.NSEW)
        frameCCD.config(borderwidth=1, relief=tk.RIDGE)
        frameCCD.config(padx=10,pady=10)

        self.ccdWidth.label1.grid(row=0,column=0,sticky=tk.W)
        self.ccdWidth.label2.grid(row=0,column=2,sticky=tk.W)
        self.ccdWidth.tBox.grid(row=0,column=1,sticky=tk.W)

        self.ccdHeight.label1.grid(row=1,column=0,sticky=tk.W)
        self.ccdHeight.label2.grid(row=1,column=2,sticky=tk.W)
        self.ccdHeight.tBox.grid(row=1,column=1,sticky=tk.W)

        self.pixelSize.label1.grid(row=2,column=0,sticky=tk.W)
        self.pixelSize.label2.grid(row=2,column=2,sticky=tk.W)
        self.pixelSize.tBox.grid(row=2,column=1,sticky=tk.W)

        self.binning.label1.grid(row=3,column=0,sticky=tk.W)
        self.binning.tBox.grid(row=3,column=1,sticky=tk.W)

        self.ccdWidth.tBox.configure(justify=tk.RIGHT)
        self.ccdHeight.tBox.configure(justify=tk.RIGHT)
        self.pixelSize.tBox.configure(justify=tk.RIGHT)
        self.binning.tBox.configure(justify=tk.RIGHT)

    ##------------------------------------------------------------------------
    ## METHOD setCCDFrame
    def setCubeTypeFrame(self,master):
        """
        This frame sets the kind of cube that will be produced using radio
        buttons.

        @param master: parent widget (e.g. a Tkinter.Frame)
        """
        frameModes = tk.Frame(master)
        frameModes.grid(row=1,column=0,sticky=tk.NSEW)
        frameModes.config(borderwidth=1, relief=tk.RIDGE)
        frameModes.config(padx=10,pady=10)
        self.mode = tk.StringVar()

        self.rb_rawCube = tk.Radiobutton(frameModes,
            text="Raw Cube",
            variable=self.mode,
            value="raw",
            name="rButton_raw")
        self.rb_rawCube.pack(anchor=tk.W)

        self.rb_imageCube = tk.Radiobutton(frameModes,
            text="Image Cube",
            variable=self.mode,
            value="image",
            name="rButton_img")
        self.rb_imageCube.pack(anchor=tk.W)

        self.rb_spectrumCube = tk.Radiobutton(frameModes,
            text="Spectrum Cube",
            variable=self.mode,
            value="spectrum",
            name="rButton_spc")
        self.rb_spectrumCube.pack(anchor=tk.W)

    ##------------------------------------------------------------------------
    ## METHOD setFilesFrame
    def setFilesFrame(self,master):
        """
        This method sets the frame that holds the widgets related to
        input/output files. Again only a contained is used has parameter.

        @param master: parent widget (e.g. a Tkinter.Frame)
        """
        frameFiles = tk.Frame(master)

        self.outFile	= sgui.FileOutput(frameFiles,label="Output filename: ")
        self.outFile.options['defaultextension'] = ".fits"
        self.outFile.options['filetypes'] = \
                            [('fits files', '.fits'), ('all files', '.*')]

        self.spcFile	= sgui.FileInput(frameFiles,label="Input spectrum: ")
        self.spcFile.options['filetypes'] = [('text files', '.txt'), ('text files', '.dat'), ('all files', '.*')]

        self.iImage		= sgui.FileInput(frameFiles,label="Input image: ")
        self.iImage.options['filetypes'] = [('fits files', '.fits')]
        self.iWLength	= sgui.Input(frameFiles,t1="Input wavelength",t2="nm")

        self.owritevar  = tk.IntVar()
        self.owrite 	= tk.Checkbutton(frameFiles,
                        text="Overwrite output files?",variable=self.owritevar)

        frameFiles.grid(row=1,column=1,stick=tk.NSEW)
        frameFiles.config(borderwidth=1, relief=tk.RIDGE)
        frameFiles.config(padx=10,pady=10)

        self.outFile.label.grid(column=0,row=0,sticky=tk.W)
        self.outFile.entry.grid(column=1,row=0,sticky=tk.E)
        self.outFile.button.grid(column=2,row=0,sticky=tk.E)

        self.iImage.label.grid(column=0,row=1,sticky=tk.W)
        self.iImage.entry.grid(column=1,row=1,sticky=tk.E)
        self.iImage.button.grid(column=2,row=1,sticky=tk.E)

        self.iWLength.label1.grid(column=0,row=2,sticky=tk.W)
        self.iWLength.label2.grid(column=2,row=2,sticky=tk.E)
        self.iWLength.tBox.grid(column=1,row=2,sticky=tk.E)

        self.spcFile.label.grid(column=0,row=3,sticky=tk.W)
        self.spcFile.entry.grid(column=1,row=3,sticky=tk.E)
        self.spcFile.button.grid(column=2,row=3,sticky=tk.E)

        self.owrite.grid(column=0,row=5,sticky=tk.W)

    ##------------------------------------------------------------------------
    ## METHOD setButtonsFrame
    def setButtonsFrame(self, master):
        """
        This method sets the frame that hold the buttons to run Illusion and
        to close it.

        @param master: parent widget (e.g. a Tkinter.Frame)
        """
        frameButtons = tk.Frame(master)
        self.BClose  = tk.Button(frameButtons, text="Close",
                                                     command=master.destroy)
        self.BRun    = tk.Button(frameButtons, text="Run", command=self.run)

        frameButtons.grid(row=2,column=1,sticky=tk.E)
        self.BClose.pack(side=tk.LEFT)
        self.BRun.pack(side=tk.LEFT)

        self.BClose.configure(width=8)
        self.BRun.configure(width=8)

    ##------------------------------------------------------------------------
    ## METHOD setSandardValues
    def setStandardValues(self):
        """
        After the whole GUI is build, the standard values are set.
        """
        self.mode.set("raw")

        self.centralWavelength.set(550.0)
        self.spectralResolution.set(20000)
        self.finesse.set(25)
        self.extrapolate.set(110)
        self.focalLength.set(350)

        self.ccdWidth.set(1600)
        self.ccdHeight.set(1600)
        self.pixelSize.set(16)
        self.binning.set(4)

        self.owritevar.set(1)

        self.outFile.set("./Data/output.fits")
        self.iImage.set("./Data/inputFrame.fits")
        self.iWLength.set(550)
        self.spcFile.set("./Data/inputSpectrum.txt")

    ##------------------------------------------------------------------------
    ## METHOD run
    def run(self):
        """
        This method controls what happens once the RUN button is pressed.

        Basically, it gets all the parameters, saves them into a config
        file and run the Illusion Engine using popen.
        """

        myConfig = ''
        myConfig += 'class Config:\n'
        myConfig += '    pass\n'

        myConfig += 'Config.type = "%s" \n' % self.mode.get()

        myConfig += 'Config.lambda_0 = %.2f \n' % self.centralWavelength()
        myConfig += 'Config.specResolution = %.2f \n' % self.spectralResolution()
        myConfig += 'Config.finesse = %.2f \n' % self.finesse()
        myConfig += 'Config.focalLength = %.2f \n' % self.focalLength()
        myConfig += 'Config.extrapolate = %.2f \n' % self.extrapolate(1.e-2)
        myConfig += 'Config.noise = %d \n' % self.noisevar.get()

        myConfig += 'Config.width = %d \n' % self.ccdWidth()
        myConfig += 'Config.height = %d \n' % self.ccdHeight()
        myConfig += 'Config.pixelSize = %d \n' % self.pixelSize()
        myConfig += 'Config.binning = %d \n' % self.binning()

        myConfig += 'Config.output = "%s" \n' % self.outFile()
        myConfig += 'Config.input_wavelength = %.2f \n' % self.iWLength()
        myConfig += 'Config.input_image = "%s" \n' % self.iImage()
        myConfig += 'Config.input_spectrum = "%s" \n' % self.spcFile()

        myConfig += 'EConfig.verbose = %d \n' % 1
        myConfig += 'EConfig.overwrite = %d \n' % self.owritevar.get()

        configFile = open('./Conf/temp_gui_config.py', 'w')
        configFile.write(myConfig)
        configFile.close()

        sproc.Popen(['python', './Engine/engine.py', './Conf/temp_gui_config.py'])

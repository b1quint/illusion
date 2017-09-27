"""
    Graphical User Interface         __   __    
    Illusion Data-Synthesizer       (  \,/  )   
    Butterfly Software System        \_ | _/    
                            	     (_/ \_) 
    Bruno Correa Quint - 2009.07.03 - v1.7.0
"""

from numpy import array
from pyfits import getdata
from Tkinter import *
from auxclasses import *

import iodata
import fpdata

#=============================================================================#
# CLASS Run                                                                   #
#=============================================================================#
class Run:
	"""
	TO DO
	"""
	#==========================================================================
	def __init__(self,master):
		"""
		TO DO
		"""
		#-------------------------------
		# Setting the main frame
		self.setMainFrame(master)
		
		#-------------------------------
		# Setting the Fabry-Perot frame
		self.setFabryPerotFrame(master)
		
		#-------------------------------
		# Setting the CCD frame
		self.setCCDFrame(master)
		
		#-------------------------------
		# Setting the CubeType frame
		self.setCubeTypeFrame(master)
		
		#-------------------------------
		# Setting the Files frame
		self.setFilesFrame(master)
		
		#-------------------------------
		# Setting the Buttons frame		
		self.setButtonsFrame(master)
		
		#-------------------------------
		self.setStandardValues()
		
		#-------------------------------
		# Setting active and inactive widgets
		self.setActives()
		
	#==========================================================================
	def setMainFrame(self,master):
		"""
		TO DO
		"""
		#------------------------------
		# Setting the windows title
		master.title("Illusion v1.7.0 - Data Cube Synthesizer")
		
		#------------------------------
		# Setting the windows' minimum size
		master.minsize(800,300)
		
		#------------------------------
		# Fixing the window's size
		master.resizable(0,0)
	
	#==========================================================================
	def setFabryPerotFrame(self,master):
		"""
		to do
		"""
		
		#------------------------------------------------------------
		# Creating input parameters
		frameFP = Frame(master)
		self.centralWavelength	= Input(frameFP,t1="Central wavelength: ",t2=" nm")
		self.spectralResolution	= Input(frameFP,t1="Spectral resolution: ")
		self.finesse            = Input(frameFP,t1="Finesse: ")
		self.extrapolate        = Input(frameFP,t1="Extrapolate: ", t2="%")
		self.focalLength        = Input(frameFP,t1="Focal length: ",t2=" mm")		
		
		#------------------------------------------------------------
		# Setting the widgets positions and layout
		frameFP.grid(row=0,column=0,sticky=N)
		frameFP.config(borderwidth=1, relief=RIDGE)
		frameFP.config(padx=10,pady=10)
		
		self.centralWavelength.label1.grid(row=0,column=0,sticky=W)
		self.centralWavelength.label2.grid(row=0,column=2,sticky=W)
		self.centralWavelength.tBox.grid(row=0,column=1,sticky=W)
		
		self.spectralResolution.label1.grid(row=1,column=0,sticky=W)
		self.spectralResolution.tBox.grid(row=1,column=1,sticky=W)
		
		self.finesse.label1.grid(row=2,column=0,sticky=W)
		self.finesse.tBox.grid(row=2,column=1,sticky=W)
		
		self.extrapolate.label1.grid(row=3,column=0,sticky=W)
		self.extrapolate.label2.grid(row=3,column=2,sticky=W)
		self.extrapolate.tBox.grid(row=3,column=1,sticky=W)
		
		self.focalLength.label1.grid(row=4,column=0,sticky=W)
		self.focalLength.label2.grid(row=4,column=2,sticky=W)
		self.focalLength.tBox.grid(row=4,column=1,sticky=W)
		
		#------------------------------------------------------------
		# Configure entry boxes
		self.centralWavelength.tBox.configure(justify=RIGHT)
		self.spectralResolution.tBox.configure(justify=RIGHT)
		self.finesse.tBox.configure(justify=RIGHT)
		self.extrapolate.tBox.configure(justify=RIGHT)
		self.focalLength.tBox.configure(justify=RIGHT)
	
	#==========================================================================
	def setCCDFrame(self,master):
		
		#------------------------------------------------------------
		# Creating input parameters
		frameCCD 	= Frame(master)
		self.ccdWidth	= Input(frameCCD,t1="Detector's width: ",t2=" pixels")
		self.ccdHeight	= Input(frameCCD,t1="Detector's height: ",t2=" pixels")
		self.pixelSize	= Input(frameCCD,t1="Pixel's size: ", t2=" microns")
		self.binning	= Input(frameCCD,t1="Binning: ")
		
		#------------------------------------------------------------
		# Setting widgets positions
		frameCCD.grid(row=0,column=1,sticky=NSEW)
		frameCCD.config(borderwidth=1, relief=RIDGE)
		frameCCD.config(padx=10,pady=10)
		
		self.ccdWidth.label1.grid(row=0,column=0,sticky=W)
		self.ccdWidth.label2.grid(row=0,column=2,sticky=W)
		self.ccdWidth.tBox.grid(row=0,column=1,sticky=W)
		
		self.ccdHeight.label1.grid(row=1,column=0,sticky=W)
		self.ccdHeight.label2.grid(row=1,column=2,sticky=W)
		self.ccdHeight.tBox.grid(row=1,column=1,sticky=W)
		
		self.pixelSize.label1.grid(row=2,column=0,sticky=W)
		self.pixelSize.label2.grid(row=2,column=2,sticky=W)
		self.pixelSize.tBox.grid(row=2,column=1,sticky=W)
		
		self.binning.label1.grid(row=3,column=0,sticky=W)
		self.binning.tBox.grid(row=3,column=1,sticky=W)
		
		#----------------------------------------------------------------------
		# Configuring entry boxes
		self.ccdWidth.tBox.configure(justify=RIGHT)
		self.ccdHeight.tBox.configure(justify=RIGHT)
		self.pixelSize.tBox.configure(justify=RIGHT)
		self.binning.tBox.configure(justify=RIGHT)
	
	#==========================================================================
	def setCubeTypeFrame(self,master):
		"""
		TO DO
		"""
		#------------------------------------------------------------
		# Creating the widgets
		frameModes = Frame(master)
		frameModes.grid(row=1,column=0,sticky=NSEW)
		frameModes.config(borderwidth=1, relief=RIDGE)
		frameModes.config(padx=10,pady=10)
		self.mode = StringVar()
		
		self.rb_rawCube = Radiobutton(frameModes, 
			text="Raw Cube", 
			variable=self.mode, 
			value="raw", 
			name="rButton_raw",
			command=self.rawCube_Action)
		self.rb_rawCube.pack(anchor=W)
				
		self.rb_imageCube = Radiobutton(frameModes, 
			text="Image Cube", 
			variable=self.mode, 
			value="img", 
			name="rButton_img",
			command=self.imageCube_Action)
		self.rb_imageCube.pack(anchor=W)
		
		self.rb_spectrumCube = Radiobutton(frameModes, 
			text="Spectrum Cube", 
			variable=self.mode, 
			value="spc", 
			name="rButton_spc",
			command=self.spectrumCube_Action)
		self.rb_spectrumCube.pack(anchor=W)
		
		self.rb_phaseCube = Radiobutton(frameModes, 
			text="Phase-Shifting Cube", 
			variable=self.mode, 
			value="psc", 
			name="rButton_psc",
			command=self.phaseCube_Action)
		self.rb_phaseCube.pack(anchor=W) 
	
	#==========================================================================
	def setFilesFrame(self,master):
		"""
		TO DO
		"""
		#------------------------------------------------------------
		# Creating widgets
		
		frameFiles = Frame(master)
		
		#-----------------------------------------------------------------------------------#
		self.outFile	= FOutput(frameFiles,label="Output filename: ")
		self.outFile.options['defaultextension'] = ".fits"
		self.outFile.options['filetypes'] = [('fits files', '.fits'), ('all files', '.*')]
		
		#-----------------------------------------------------------------------------------#
		self.spcFile	= FInput(frameFiles,label="Input spectrum: ")
		self.spcFile.options['filetypes'] = [('fits files', '.fits')]
		
		#-----------------------------------------------------------------------------------#
		self.iImage		= FInput(frameFiles,label="Input image: ")
		self.iImage.options['filetypes'] = [('fits files', '.fits')]
		self.iWLength	= Input(frameFiles,t1="Image wavelength",t2="nm")
		
		#-----------------------------------------------------------------------------------#
		self.iCube   	= FInput(frameFiles,label="Input cube: ")
		self.iCube.options['filetypes'] = [('fits files', '.fits')]
		
		self.owritevar  = IntVar()
		self.owrite 	= Checkbutton(frameFiles,text="Overwrite output files?",variable=self.owritevar)
		
		#------------------------------------------------------------
		# Organizing the widgets
		frameFiles.grid(row=1,column=1,stick=NSEW)
		frameFiles.config(borderwidth=1, relief=RIDGE)
		frameFiles.config(padx=10,pady=10)
		
		self.outFile.label.grid(column=0,row=0,sticky=W)
		self.outFile.entry.grid(column=1,row=0,sticky=E)
		self.outFile.button.grid(column=2,row=0,sticky=E)
		
		self.iImage.label.grid(column=0,row=1,sticky=W)
		self.iImage.entry.grid(column=1,row=1,sticky=E)
		self.iImage.button.grid(column=2,row=1,sticky=E)
		
		self.iWLength.label1.grid(column=0,row=2,sticky=W)
		self.iWLength.label2.grid(column=2,row=2,sticky=E)
		self.iWLength.tBox.grid(column=1,row=2,sticky=E)
		
		self.spcFile.label.grid(column=0,row=3,sticky=W)
		self.spcFile.entry.grid(column=1,row=3,sticky=E)
		self.spcFile.button.grid(column=2,row=3,sticky=E)
		
		self.iCube.label.grid(column=0,row=4,sticky=W)
		self.iCube.entry.grid(column=1,row=4,sticky=E)
		self.iCube.button.grid(column=2,row=4,sticky=E)
		
		self.owrite.grid(column=0,row=5,sticky=W)
	
	#==========================================================================
	def setButtonsFrame(self,master):
		#------------------------------------------------------------
		# Creating widgets
		frameButtons = Frame(master)
		self.BClose  = Button(frameButtons, text="Close", command=master.destroy)
		self.BRun    = Button(frameButtons, text="Run", command=self.run)
		
		#------------------------------------------------------------
		# Organizing widgets
		frameButtons.grid(row=2,column=1,sticky=E)
		self.BClose.pack(side=LEFT)
		self.BRun.pack(side=LEFT)
		
		self.BClose.configure(width=8)
		self.BRun.configure(width=8)
	
	#==========================================================================
	def setActives(self):
		#------------------------------------------------------------
		# Turning on the overwrite option
		self.owrite.select()
		
		#------------------------------------------------------------
		# Setting Raw Cube as the standard
		self.rb_rawCube.select()
		self.rawCube_Action()
	
	#==========================================================================
	def rawCube_Action(self):
		
		self.spcFile.disable()
		self.iImage.disable()
		self.iWLength.disable()
		self.iCube.disable()
	
	#==========================================================================
	def imageCube_Action(self):
		self.spcFile.disable()
		self.iImage.enable()
		self.iWLength.enable()
		self.iCube.disable()
	
	#==========================================================================
	def spectrumCube_Action(self):
		self.spcFile.enable()
		self.iImage.disable()
		self.iWLength.disable()
		self.iCube.disable()
	
	#==========================================================================
	def phaseCube_Action(self):
		self.spcFile.disable()
		self.iImage.disable()
		self.iWLength.disable()
		self.iCube.enable()
	
	#==========================================================================
	def run(self):
		disable(self.BRun)
		
		fp = fpdata.FabryPerot( 
					self.centralWavelength(1e-3), 
					self.spectralResolution(), 
					self.finesse(), 
					self.focalLength(1.e3), 
					extrapolate = self.extrapolate(1.e-2),
					verbose=1
					)
		
		ccd = fpdata.Detector(
					int( self.ccdWidth() / self.binning() ), 
					int( self.ccdHeight() / self.binning() ), 
					fp.nPoints, 
					int( self.pixelSize() * self.binning())
					)
		
		#-------------------------------------------------------------
		if self.mode.get() == "raw":
			print ">>> Creating a raw cube..."
			fp.raw_cube(ccd)
			ccd.set_header(fp)
			iodata.writeFits( 
					self.outFile(), 
					ccd.data, 
					ccd.header, 
					overwrite=self.owritevar.get()
					)
		
		#---------------------------------------------------------------
		elif self.mode.get() == "img":
			print ">>> I'm running the program for a Image Cube!"
			print ">> Reading image..."
			rawImage = getdata( self.iImage() )
			print ">> Creating the cube..."
			fp.imageCube(ccd, rawImage, self.iWLength(1e-3) )
			ccd.set_header(fp)
			iodata.writeFits( 
					self.outFile(), 
					ccd.data, 
					ccd.header, 
					overwrite=self.owritevar.get()
					)
		
		#----------------------------------------------------------------
		elif self.mode.get() == "spc":
			print "I'm running the program for a Spectrum Cube!"
			spec = iodata.readEmLines( self.spcFile() )
			spec[:,0] *= 1e-3 
			fp.specCube(ccd,spec)
			ccd.set_header(fp)
			iodata.writeFits( 
					self.outFile(), 
					ccd.data, 
					ccd.header,
					overwrite=self.owritevar.get()
					)
		
		#-----------------------------------------------------------------
		elif self.mode.get() == "psc":
			print "I'm running the program for a Phase-Shifting Cube!"
			print "Reading cube..."
			cube = getdata(self.iCube())
			print "Populating cube..."
			fp.dephasedCube(ccd, cube, [1,10,20])
			print "Setting header..."
			ccd.set_header(fp)
			print "Exporting data...."
			iodata.writeFits( 
					self.outFile(),
					ccd.data, 
					ccd.header, 
					overwrite=self.owritevar.get(),
					verbose=1
					)
		
		else: 
			raise "Cube type not defined"
		
		enable(self.BRun)
		print '\a'

	def setStandardValues(self):
		
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
		
		self.outFile.set("output.fits")
		self.iImage.set("inputFrame.fits")
		self.iWLength.set(550)
		self.spcFile.set("inputSpectrum.txt")
		self.iCube.set("inputCube.fits")
		
	def test(self):
		print "Ok! I'm working!"

#=========================================================================#
# GLOBAL METHOD enable                                                    #
#=========================================================================#
def enable(widget):
	widget.config(state=NORMAL)

#=========================================================================#
# GLOBAL METHOD disable                                                   #
#=========================================================================#
def disable(widget):
	widget.config(state=DISABLED)



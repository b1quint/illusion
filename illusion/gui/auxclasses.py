"""
	    __   __    
	   (  \,/  )   
	    \_ | _/    
	    (_/ \_)  
	
	   Butterfly 
	Software System
	
	@author: Bruno Correa Quint
	@date:   May-14-2009
	
	This package is part of Illusion Data-Cube Synthesizer Package for BTFI.
	This package contains some classes that helps the GUI code to be easier to write/read.
	
	Please, read the LICENSE file for more information about copy and distribution.

"""

from Tkinter import Button, DISABLED, END, Entry, Label, NORMAL, PhotoImage
import tkFileDialog

#===================================================================#
# CLASS Input                                                       #
#===================================================================#
class Input:
	"""
	(TO DO)
	"""
	#================================================================
	def __init__(self,master,t1="x",t2="",name=""):
		"""
		(TO DO)
		"""
		
		if name == "":
			self.label1 = Label(master, text=t1)
			self.label2 = Label(master, text=t2)
			self.tBox   = Entry(master)
			
		else:
			self.label1 = Label(master, text=t1, name=("lb1_"+name))
			self.label2 = Label(master, text=t2, name=("lb2_"+name))
			self.tBox   = Entry(master, name=("tbox_"+name))

	#================================================================
	def __call__(self,cFactor=1.):
		"""
		(TO DO)
		"""
		return self.get(cFactor)

	#===============================================================
	def get(self,cFactor=1.):
		"""
		(TO DO)
		"""
		
		tmp = float( self.tBox.get() )
		return  tmp * cFactor

	#================================================================
	def set(self,value):
		"""
		(TO DO)
		"""
		self.tBox.delete(0,END)
		self.tBox.insert(0,value)

	#================================================================
	def enable(self):
		"""
		(TO DO)
		"""
		self.label1.config(state=NORMAL)
		self.label2.config(state=NORMAL)
		self.tBox.config(state=NORMAL)
		
	#================================================================
	def disable(self):
		"""
		(TO DO)
		"""
		self.label1.config(state=DISABLED)
		self.label2.config(state=DISABLED)
		self.tBox.config(state=DISABLED)

#===================================================================#
# CLASS FInput                                                     #
#===================================================================#	
class FInput:
	""" Class created to manipulate files for output """
	def __init__(self, master, label=""):
		
		self.label = Label(master, text=label)
		self.entry = Entry(master)
		self.button = Button(master, text="Open", command=self.getLoadName)
		self.options = {}
	
	def __call__(self):
		return self.entry.get()

	def set(self, value):
		self.entry.delete(0,END)
		self.entry.insert(0,value)

	def setOptions(self, options):
		""" Getting the options """
		self.options = options
	
	def getLoadName(self):
		""" The method that takes the filename """
		filename = tkFileDialog.askopenfilename(**self.options)
		self.entry.delete(0,END)
		self.entry.insert(0,filename)
	
	def enable(self):
		self.label.config(state=NORMAL)
		self.entry.config(state=NORMAL)
		self.button.config(state=NORMAL)
	
	def disable(self):
		self.label.config(state=DISABLED)
		self.entry.config(state=DISABLED)
		self.button.config(state=DISABLED)
	
#===================================================================#
# CLASS FOutput                                                     #
#===================================================================#	
class FOutput:
	""" Class created to manipulate files for output """
	def __init__(self, master, label=""):
		
		#icon = PhotoImage(file="open.gif")
		self.label = Label(master, text=label)
		self.entry = Entry(master)
		self.button = Button(master, text="Save", command=self.getLoadName)
		self.options = {}
	
	def __call__(self):
		return self.entry.get()
	
	def set(self, value):
		self.entry.delete(0,END)
		self.entry.insert(0,value)
	
	def setOptions(self, options):
		""" Getting the options """
		self.options = options
	
	def getLoadName(self):
		""" The method that takes the filename """
		filename = tkFileDialog.asksaveasfilename(**self.options)
		self.entry.delete(0,END)
		self.entry.insert(0,filename)
	
	def enable(self):
		self.label.config(state=NORMAL)
		self.entry.config(state=NORMAL)
		self.button.config(state=NORMAL)
	
	def disable(self):
		self.label.config(state=DISABLED)
		self.entry.config(state=DISABLED)
		self.button.config(state=DISABLED)


#===================================================================#
# Method ProgressBar                                                #
#===================================================================#
def progressBar(value, max, barsize):
	import sys
	chars = int(value * barsize / float(max))
	percent = int((value / float(max)) * 100)
	sys.stdout.write("# ")
	sys.stdout.write("*" * chars)
	sys.stdout.write(" " * (barsize - chars + 2))
	if value >= max:
		sys.stdout.write("Done. \n")
	else:
		sys.stdout.write("[%3i%%]\r" % (percent))
		sys.stdout.flush()		
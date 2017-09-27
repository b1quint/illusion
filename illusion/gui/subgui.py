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
# Sub-classes created to customize Tkinter widgets.
"""

import tkFileDialog
import Tkinter as tk

##============================================================================
## CLASS Input                                                       
class Input:
    """
    A class containing set of widgets composed by two labels and a text field. 
    One label to describe the variable, the text field to receive it and the 
    second label for units.
    """

    ##------------------------------------------------------------------------
    ## METHOD __init__
    def __init__(self,master,t1="x",t2=""):
        """
        The set constructor. 
        
        @param master: parent widget (e.g. a Tkinter.Frame)
        @param t1: a string with a short description of the variable.
        @param t2: a string containing the input's units.
        """
        
        self.label1 = tk.Label(master, text=t1)
        self.label2 = tk.Label(master, text=t2)
        self.tBox   = tk.Entry(master)
    
    ##------------------------------------------------------------------------
    ## METHOD __call__
    def __call__(self, cFactor=1.):
        """
        This method parses the contents of the text field to float and returns
        its value. A conversion factor can be used as an option.
        
        @param cFactor: a float number representing the conversion factor 
                        from a unit to other, e.g. from "nm" to "m" it would 
                        be 1e-9 (optional).
        """
        tmp = float( self.tBox.get() )
        return  tmp * cFactor

    ##------------------------------------------------------------------------
    ## METHOD set
    def set(self,value):
        """
        This method is used to print a number in the text field.
        
        @param value: float number to be displayed. 
        """
        self.tBox.delete(0,tk.END)
        self.tBox.insert(0,value)
    
    ##------------------------------------------------------------------------
    ## METHOD enable
    def enable(self):
        """
        Method to enable the widgets. 
        
        To understand better what "enabled" means in TkInter context, please
        read the TkInter.Widget.config documentation.
        """
        self.label1.config(state=NORMAL)
        self.label2.config(state=NORMAL)
        self.tBox.config(state=NORMAL)
    
    ##------------------------------------------------------------------------
    ## METHOD disable
    def disable(self):
        """
        Method to enable the widgets. 
        
        To understand better what "enabled" means in TkInter context, please
        read the TkInter.Widget.config documentation.
        """
        self.label1.config(state=DISABLED)
        self.label2.config(state=DISABLED)
        self.tBox.config(state=DISABLED)

##============================================================================
## CLASS FIO
class FileIO:
    """
    Class containing the basic widgets ?????????????????
    
    A class containing set of widgets composed by a labels and a text field
    to handle filenames for reading. The label is a short description of the
    file that shall be read and the text field receives a string containg
    the address of this file.
    """
    ##------------------------------------------------------------------------
    ## METHOD __init__
    def __init__(self, master, label=""):
        """
        Class constructor.
        
        @param master: parent widget (e.g. a Tkinter.Frame)
        @param label: a string with a short description of the variable.
        """
        self.label = tk.Label(master, text=label)
        self.entry = tk.Entry(master)
        self.button = tk.Button(master, text="Open", command=self.getLoadName)
        self.options = {}
    
    ##------------------------------------------------------------------------
    ## METHOD __call__
    def __call__(self):
        """
        This method returns the contents of the text field.
        """
        return self.entry.get()
    
    ##------------------------------------------------------------------------
    ## METHOD set
    def set(self, value):
        """
        This method is used to print a number in the text field.
        
        @param value: float number to be displayed. 
        """
        self.entry.delete(0,tk.END)
        self.entry.insert(0,value)

    ##------------------------------------------------------------------------
    ## METHOD setOptions:
    def setOptions(self, options):
        """
        tkFileDialog module uses a dictionary to set the options of a file
        dialog. This method allows the class to receive a dictionary
        with these options.

        @param options: a dictionary containing 
        """ 
        self.options = options
    
    ##------------------------------------------------------------------------
    ## METHOD enable
    def enable(self):
        """
        Method to enable the widgets. 
        
        To understand better what "enabled" means in TkInter context, please
        read the TkInter.Widget.config documentation.
        """
        self.label1.config(state=NORMAL)
        self.label2.config(state=NORMAL)
        self.tBox.config(state=NORMAL)
    
    ##------------------------------------------------------------------------
    ## METHOD disable
    def disable(self):
        """
        Method to enable the widgets. 
        
        To understand better what "enabled" means in TkInter context, please
        read the TkInter.Widget.config documentation.
        """
        self.label1.config(state=DISABLED)
        self.label2.config(state=DISABLED)
        self.tBox.config(state=DISABLED)
        
##============================================================================
## CLASS FInput
class FileInput(FileIO):
    """
    A class containing set of widgets composed by a labels and a text field
    to handle filenames for reading. The label is a short description of the
    file that shall be read and the text field receives a string containg
    the address of this file.
    """
    ##------------------------------------------------------------------------
    ## METHOD getLoadName
    def getLoadName(self):
        """
        This method uses tkFileDialog to find for a file and puts its name in 
        the text field. 
        """
        filename = tkFileDialog.askopenfilename(**self.options)
        self.entry.delete(0,tk.END)
        self.entry.insert(0,filename)
    
    
##============================================================================
## CLASS FOutput
class FileOutput(FileIO):
    """
    A class containing set of widgets composed by a labels and a text field
    to handle filenames for writing. The label is a short description of the
    file that shall be written and the text field receives a string containg
    the address of this file.
    """
    ##------------------------------------------------------------------------
    ## METHOD getLoadName
    def getLoadName(self):
        """
        This method uses tkFileDialog to find for a file and puts its name in 
        the text field. 
        """
        filename = tkFileDialog.asksaveasfilename(**self.options)
        self.entry.delete(0,tk.END)
        self.entry.insert(0,filename)

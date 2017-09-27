"""
	    __   __    
	   (  \,/  )   
	    \_ | _/    
	    (_/ \_)  
	
	   Butterfly 
	Software System
	
	@author: Bruno Correa Quint
	@date: Mar-19-2009
	
	This package is part of Illusion Data-Cube Synthesizer Package for BTFI.
	This package contains methods to import data from files and export data to them.
	
	Please, read the LICENSE file for more information about copy and distribution.
	
"""
import os.path
from pyfits import getdata, getheader, writeto
from scipy import array, float32, loadtxt

try:
    from pylab import cm, imshow, savefig
    from pylab import title as imtitle
except ImportError:
    print "WARNING: Failed to load modules from MatPlotLib."
    pass


#==========================================================
def findNewFilename( filename):
	"""
	Method create to find filenames availabe for exporting data. 
	The returned filename will be the same in the beggining but
	it will contain a number in the end.
	
	@param filename: one of the candidates. 
	
	**kwargs:
	"""
	i = 1
	fileExists = 1
	while (fileExists):
		tmp = filename.split('_')
		if len(tmp) > 1:
			name = tmp[0] + '%02d_'%i + tmp[1]	
		else:
			tmp = filename.split('.')
			name = tmp[0] + '%02d.'%i + tmp[1]	
		i += 1
		fileExists = os.path.exists(name)
	return name
	
#==========================================================!
def readEmLines( filename ):
	"""
	Read a text file containing information about emission lines.
	The first column must be the wavelength in microns and the 
	second value is its intensity.
	
	@param filename: the name of the file that contains the data.
	"""
	try:
		s = loadtxt(filename)
	except (IOError):
		errorMessage =    "# Ooops! The input text file containing the emission lines does not exist.\n"
		errorMessage += "# Please, check again the config file and run again."
		print errorMessage
		raise IOError, errorMessage
	if s.ndim == 1: s = s.reshape((1,2))
	return s
	
#==========================================================
def readFits( filename ):
	"""
	Read a FITS file and return its data and its header.
	
	@param filename: The name of the file containing data.
	"""
	try: 
		data 	= getdata( filename )
		hdr 		= getheader( filename )
	except (IOError):
		errorMessage =    "# Ooops! The input fits file does not exist.\n"
		errorMessage += "# Please, check again the config file and run againg."
		print errorMessage
		raise IOError, errorMessage
	return data, hdr

#==========================================================
def writeFits( filename, data, header=None, **kwargs ):
	"""
	Export data in a fits file.
		
	This method is used to export the 'dataArray'	(2D or 3D numpy-array data) to a fits file. 
	If the data is not a valid numpy.array data, it raises an error informing it. 
		
	@param 	filename: A string containing the output filename.	
	@param 	data: A 2D or 3D numpy.array data containing the information to be stored in the
	fits file.
	
	@arg 	header: A header to be stored in the fits header. The default is 'None'.
	
	@kwarg 	verbose: Do you want to run in verbose mode? (1 - Yes, 0 - No)
	@kwarg	overwrite: Do you want to overwrite existing files? (1 - Yes, 0 - No)
	"""
	# .: Setting options :. 
	verbose, overwrite = 0, 0
	for key in kwargs:
		if key == 'verbose':
			verbose = kwargs[key]
		if key == 'overwrite':
			overwrite = kwargs[key]

	# .: Does the file exist? If so, delete it or create a new one? :.
	if os.path.exists( filename ):
		if overwrite:
			if verbose: print "# Overwriting file..."
			os.remove( filename )
		else:
			if verbose: print "# Creating a new file..."
			filename = findNewFilename( filename )

	# .: Exporting data :.
	if verbose: print "# Exporting image: ", filename
	writeto( filename, data, header )

#==========================================================
def writePNG( filename, data, **kwargs ):
	"""
	Write a single frame to a PNG file or a data-cube to a set of PNF files.
	
	@param filename: The name of the file that will be exported in the case of a single
	frame or the kernel of the names of the files that will be exported in the case of a 
	datacube.
	
	@para data: a 2D or 3D numpy array.
	
	**kwargs:
	verbose:	do you want to enter in verbose mode? ( 1 = yes, 0 = no )
	color: what kind of colors do you want? 'gray', 'heat' or  'rainbow' (default)
	overwrite: do you want to overwrite existing files? ( 1 = yes, 0 = no )
	title: What is your image name? (Write a string)
	"""
	# .: Setting the options :.
	verbose, overwrite, title = 0, 0, ''
	color = None
	for key in kwargs:
		if key == 'verbose':
			verbose = kwargs[key]
		if key == 'color':
			color = kwargs[key]
		if key == 'overwrite':
			overwrite = kwargs[key]
		if key == 'title':
			title = kwargs[key]
	# .: Is it a 2D data? A 3D data? Or none of them? Export them!:.
	if data.ndim == 2:
		write2DPNG( filename, data, verbose=verbose, color=color, overwrite=overwrite )
	elif data.ndim == 3: 
		write3DPNG( filename, data, verbose=verbose, color=color, overwrite=overwrite )
	else: 
		errorMessage = "# Error@illusion.iodata.writePNG \n"
		errorMessage += "# Input data is not a 2D nor a 3D valid numpy array"
		print errorMessage
		raise TypeError, errorMessage

#==========================================================
def write2DPNG( filename, data, **kwargs ):
	"""
	Write a single frame to a PNG file.
	
	@param filename: The name of the file that will be exported.
	
	@para data: a 2D numpy array.
	
	**kwargs:
	verbose:	do you want to enter in verbose mode? ( 1 = yes, 0 = no )
	color: what kind of colors do you want? 'gray', 'hot' or  'rainbow' (default)
	overwrite: do you want to overwrite existing files? ( 1 = yes, 0 = no )
	title: What is your image name? (Write a string)
	"""
	# .: Setting the options :.
	verbose, overwrite, title = 0, 0, ''
	color = None
	for key in kwargs:
		if key == 'verbose':
			verbose = kwargs[key]
		if key == 'color':
			if kwargs[key] == 'gray':
				color = cm.gray
			if kwargs[key] == 'hot':
				color = cm.hot
			if kwargs[key] == 'rainbow':
				color = None
		if key == 'overwrite':
			overwrite = kwargs[key]
		if key == 'title':
			title = kwargs[key]
	
	# .: Does the file exist? If so, delete it or create a new one? :.
	if os.path.exists( filename ):
		if overwrite:
			if verbose: print "# Overwriting file..."
			os.remove( filename )
		else:
			if verbose: print "# Creating a new file..."
			filename = findNewFilename( filename )
	
	# .: Creating the image :.
	if verbose: print "# Exporting image: ", filename
	imtitle( title )
	im = imshow( data, vmin=data.min(), vmax=data.max(), 
				       cmap=color, interpolation='nearest' )
	savefig( filename )
	
	
#==========================================================
def write3DPNG( filename, data, **kwargs ):
	"""
	Write a single frame to a PNG file or a data-cube to a set of PNF files.
	
	@param filename: The kernel of the names of the files where the data will be exported.
	
	@param data: a 3D numpy array.
	
	**kwargs:
	verbose:	do you want to enter in verbose mode? ( 1 = yes, 0 = no )
	color: what kind of colors do you want? 'gray', 'heat' or  'rainbow' (default)
	overwrite: do you want to overwrite existing files? ( 1 = yes, 0 = no )
	title: What is your image name? (Write a string)
	"""
	# .: Setting the options :.
	verbose, overwrite, title = 0, 0, ''
	color = None
	for key in kwargs:
		if key == 'verbose':
			verbose = kwargs[key]
		if key == 'color':
			if kwargs[key] == 'gray':
				color = cm.gray
			if kwargs[key] == 'hot':
				color = cm.hot
			if kwargs[key] == 'rainbow':
				color = None
		if key == 'overwrite':
			overwrite = kwargs[key]
		if key == 'title':
			title = kwargs[key]
	
	# .: Adding counter to filename
	nFiles = data.shape[0]
	tmp = filename.split('.')
	kernel, backend = tmp[:-1], tmp[-1]
	for n in range(nFiles):
		filename = kernel + "_%02d."%n + backend
		# .: Does the file exist? If so, delete it or create a new one? :.	
		if os.path.exists( filename ):
			if overwrite:
				if verbose: print "# Overwriting file..."
				os.remove( filename )
			else:
				if verbose: print "# Creating a new file..."
				filename = findNewFilename( filename )
		# .: Creating the image :.
		if verbose: print "# Exporting image: ", filename
		imtitle( title )
		im = imshow( data[n], vmin=data.min(), vmax=data.max(), 
				       cmap=color, interpolation='nearest' )
		savefig( filename )
		if verbose: "# Exported image: ", filename
	
	
	
	
	
	
	
	
	
	
	
	
	

"""
	    __   __    
	   (  \,/  )   
	    \_ | _/    
	    (_/ \_)  
	
	   Butterfly 
	Software System
	
	@author: Bruno Correa Quint
	@date: Mar-17-2009
	
	This package is part of Illusion Data-Cube Synthesizer Package for BTFI.
	This package contains methods used for data manipulation as fitting functions.
	
	Please, read the LICENSE file for more information about copy and distribution.
	
"""
from scipy	import arange, empty_like, exp, random, zeros
from scipy	import optimize 
from objects 	import Gaussian, Parameter

#==========================================================
def addPoisson( data, nFactor = 1 ):
	"""
	This method is used to generate random noise on a spectrum, image or cube
	by using the numpy.random.poisson library.
		
	Parameters:
	@param data: it can be a 1D, 2D or 3D numpy-array.
		
	*args:
	nFactor: float number that is used to turn the poisson noise a float by multiplying the
	poisson distribution by it and dividing the random number resulted from the method
	by it.
		
	It returns a data with the same type that the one inputted.
	
	"""
	
	if ( data.ndim == 1 ):
		tmp = empty_like( data )
		for k in range( data.shape[0] ):
			tmp[k] = random.poisson( nFactor * data[k] ) / nFactor
	
	elif ( data.ndim == 2 ):
		tmp = empty_like( data )
		for i in range( data.shape[0] ):
			for j in range( data.shape[1] ):
				tmp[i][j] = random.poisson( nFactor * data[i][j] ) / nFactor
	
	elif ( data.ndim == 3 ):
		tmp = empty_like( data )
		for k in range( data.shape[0] ):
			for i in range( data.shape[1] ):
				for j in range( data.shape[2] ):
					tmp[k][i][j] = random.poisson( nFactor * data[k][i][j] ) / nFactor
	else: 
		errorMessage = "Error @  illusion.datamanip.addPoissonNoise: \n"
		errorMessage += "Data with more than 3 dimensions are not supported"
		raise TypeError, errorMessage
	return tmp

#==========================================================
def collapseCube( cube ):
	"""
	Collapse all frames from a cube in a single frame by adding all of them.
	
	@param cube: Cube to be collapsed.
	
	@return image: Collapsed frame.
	"""
	image = zeros( (cube.shape[1], cube.shape[2]), dtype = cube.dtype)
	for k in range( cube.shape[0] ):
		image += cube[k]
	return image
	
#==========================================================
def convolveSpectrum( cube, function ):
	"""
	Convolve the spectrum of a data cube by a given function.
	
	@param cube: Cube to be convolved.
	@param function: this must be a python instance with one arg and one return numbers.
	
	@return scube: The spectral convolved cube.
	"""
	width 	= cube.shape[1]
	height 	= cube.shape[2]
	scube 	= empty_like( cube )
	
	for i in range( width ):
		for j in range( height ):
			scube[:,i,j] = convolve1d( cube[:,i,j], function )

	return scube
	
#==========================================================
def convolve1d( data, function ):
	"""
	Convolve the numpy array Y by a function given by the user. This method is different 
	from the others exactly because of this behaviour of having a function as input. 
	Obviously, this input method has to have only one argument as input and must 
	return a number or, else, Python will give an unpredictible error.
	
	@param Y: the data to be convolved. It has to be a numpy.array
	@param function: this must be a python instance with one arg and one return numbers.
	
	@return conv: convolved data.
	"""
	# Checking if Y is a numpy.array
	if ( data.__class__ != (zeros(0).__class__) ):
		errorMessage = "Error @ illusion.datamanip.convolve1d:"
		errorMessage += "\n           The first argument is not a valid array"
		raise TypeError, errorMessage
		
	P, Q, N = data.size, 2*data.size, 3*data.size
	
	newP = zeros( N, dtype=data.dtype )
	conv	 = zeros( P, dtype=data.dtype )	
	
	newP[P:Q] = data[:] 

	for k in range(P):
		tmp = 0
		for i in range(Q):
			tmp = tmp + newP[ i + k ] * function( i - P ) 
			# tmp = tmp + newP[ i + k ] * newQ[ i ]
		conv[k] = tmp

	return conv

#==========================================================
def cubeXframe( cube, image ):
    """
    2D x 3D product
        
    This method takes each cube's frame and performs a simple multiplication of this frame 
    with the flat image inputted. On this multiplication the pixels are multiplied one by one.
        The cube and the frame have to have the same width and heigh.
    
    @param 	cube: a 3D numpy.array representing the data cube.
    @param 	image: a 2D numpy.array representing the image frame.
    
    @return 	result: a 3D numpy.array representing the multiplied cube.
    
    """
    # .: Let us multiply :. 
    result = empty_like( cube )
    #print image.shape, cube.shape
    for k in range( cube.shape[0] ):
        for i in range( cube.shape[1] ):
            for j in range( cube.shape[2] ):
                result[k,i,j] = cube[k,i,j] * image[i,j]
    return result

#==========================================================
def index1D( data, value ):
	"""
	Find the position that a values is placed inside an array or tuplet.
	
	@param data: a one dimensional tuplet or numpy.ndarray.
	@param value: the value which position will be returned.
	
	@returns: a single value or a tuplet containing the position(s) of the value that one desired to search.
	"""
	i, imax = 0, []
	for d in data:
		if d == value:
			imax.append( i )
		i += 1
	return imax

#==========================================================
def fit( function, parameters, y, x = None ):
	"""
	Fit general data to general functions. Obviously, the shape of the function must be close to the shape of the data.
	
	It returns a list with the optimized parameters found using least-squares and an 1 if succeded.
	
	@param function: a method instance in Python. 
	@param parameters: a list containing the initial parameters.
	@param y: the data to be fitted in the function.
	
	args:
	@param x = None: the absciss values of data. If 'None' is given, it creates an array using 'numpy.arange'.
	
	@return parameters, success: It returns a list of parameters and the number 1 to indicate the sucess of the fitting process.
	"""
	if x is None: x = arange(y.shape[0])
	def f(params):
		i = 0 
		for p in parameters:
			p.set( params[i] )
			i += 1
		return y - function(x)
	p = [param() for param in parameters]
	return optimize.leastsq(f, p)

#==========================================================
def fitGaussian( data ):
	"""
	Fit a gaussian function to the data centering the gaussian peak in the maximum value found in the data.
	
	@param data: A one dimensional array with a gaussian profile looking.
	
	@return p: the three main gaussian parameters.
	@return function: a python instance of the gaussian function intialized with the three parameters found.
	"""
	center = ( index1D( data, data.max() ) )
	gauss = Gaussian( center = center[0] )	
	p, sucess = fit( gauss.function, gauss.getPars(), data )
	gauss = Gaussian( center = p[0], width = p[1], height = p[2] )
	
	return gauss
	

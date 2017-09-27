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
	This package contains several classes used in Illusion Package.
	
	Please, read the LICENSE file for more information about copy and distribution.
	
"""
from math import exp
from scipy import array, zeros
from scipy import exp as EXP
#==========================================================
class Delta:
	"""
	Object created to store the position of a Kroeninger Delta Function in one dimension. 
	This delta has value equals to the amplitude setted ( 1 as default ) if x is equal the center position and 0 otherwise.
	"""
	def __call__( self, x ):
		"""
		Delta Function. 
		
		It returns the value of the delta function using this object's parameters.
		
		@param x: input X value used to evaluate the function. x can be a number or an numpy.array.
		"""
		return self.function( x ) 

	def __init__(self, center=0, amp = 1):
		"""
		Delta Object constructor.
		
		args:
		@param center=0: if no value is given here, the delta function will be centered at
		zero. Otherwise, it will be centered in the given value.
		"""
		self.center 	= Parameter(center)
		self.amp 		= Parameter(amp)
	
	def __str__(self):
		return "f[x] = %0.1f * Delta1D( x - %0.1f )"%(self.amp(),self.center())
	
	def function( self, x ):
		"""
		Delta Function. 
		
		It returns the value of the delta function using this object's parameters.
		
		@param x: input X value used to evaluate the function. x can be a number or an numpy.array.
		"""
		# .: x is a number :.
		if ( x.__class__ == (0).__class__ ) or ( x.__class__ == (0.).__class__ ):
			if ( abs( x - self.center() ) < 1e-8 ):
				return self.amp()
			else: 
				return 0.
		# .: x is an array :.
		if (x.__class__ == (zeros(1)).__class__):
			y = zeros( x.size, x.dtype )
			for i in range( x.size ):
				if ( abs( x[i] - self.center() ) < 1e-8 ):
					y[i] = self.amp()
				else:
					y[i] = 0.
			return y

	def getAmplitude( self):
		"""
		Returns the delta's amplitude value.
		"""
		return self.amp()

	def getCenter( self):
		"""
		Returns the delta's center position.
		"""
		return self.center()
	
	def setAmplitude( self, amp):
		"""
		Sets the delta's amplitude value.
		
		@param amp: The new gaussian's amplitude value.
		"""
		self.amp 	= Parameter(amp)
	
	def setCenter( self, center):
		"""
		Sets the delta's center position.
		
		@param center: The new gaussian's center position.
		"""
		self.center 	= Parameter(center)
	
#==========================================================
class Gaussian:
	"""
	Object created to store the three main parameters that describe
	an gaussian funcion in one dimension. These three parameters are:
	the position of the center of the gaussian, the gaussian width of the function
	(not the FWHM yet) and its intensity exactly at the center. Here, the object can
	be initialized with no arguments or setting everything on it.
	
	**kwargs:
	@param center: initialize the object storing the position of the center of the gaussian.
	@param width: initialize the object storing the gaussian's width. Not the FWHM.
	@param height: initialize the object storing the height at the center.
	
	"""
	def __call__(self):
		"""
		Returns the three parameters that defines a gaussian in the following order:
		[ Center, Width, Height ]
		"""
		return [ self.center(), self.width(), self.height() ]

	def __init__(self, **kwargs):
		"""
		Gaussian object constructor.
		
		**kwargs:
		@param center: The center of the gaussian peak.
		@param width: The gaussian's width.
		@param height: The maximum value.
		
		"""
		center	= 0.
		width 	= 1.
		height 	= 1.
		for key in kwargs:
			if key == 'center':
				center = kwargs[key]
			if key == 'width':
				width = kwargs[key]
			if key == 'height':
				height = kwargs[key]
			
		self.center 	= Parameter(center)
		self.width 	= Parameter(width)
		self.height 	= Parameter(height)
	
	def __str__(self):
		return "f[x] = %0.2f * exp( -(x - %0.2f)^2 / (%0.2f)^2 )"%(self.height(),self.center(),self.width())

	def function( self, x ):
		"""
		Gaussian Function. 
		
		It returns the value of the gaussian function using this object's parameters.
		
		@param x: input X value used to evaluate the function. It can be a single number 
		or a one dimensional numpy.array
		"""
		if ( x.__class__ == (0.).__class__ ) or ( x.__class__ == (0).__class__ ):
			return self.height() * exp( -1. * ( (x - self.center())/(self.width()))**2 )
		elif ( x.__class__ == (zeros(1)).__class__ ):
			return self.height() * EXP( -1. * ( ((x - self.center())/(self.width()))**2 ) )
		else:
			raise TypeError, "Input parameter is not a valid number nor a valid array" 

	def getCenter(self):
		"""
		Returns the gaussian's center position.
		"""
		return self.center()
	
	def getFWHM(self):
		"""
		Returns the gaussian's full width at half maximum.
		"""
		# Conversion factor from width to FWHM
		# This factor is equal to 2 * sqrt( ln (2) )
		cFactor 		= 1.6651092223153954 
		return ( self.width() * cFactor ) 
	
	def getHeight(self):
		"""
		Returns the gaussian's maximum value.
		"""
		return self.height()

	def getPars(self):
		"""
		Returns the three parameters that defines a gaussian in the following order:
		[ Center, Width, Height ]
		"""
		return [ self.center, self.width, self.height ]

	def getWidth(self):
		"""
		Returns the gaussian's width. (not the FWHM)
		"""
		return self.width()

	def setCenter(self, center):
		"""
		Sets the gaussian's center position.
		
		@param center: The new gaussian's center position.
		"""
		self.center 	= Parameter(center)
	
	def setFWHM(self, fwhm):
		"""
		Sets the gaussian's width using the FWHM as input
		
		@param fwhm: The new gaussian full width at half maximum.
		"""
		# Conversion factor from width to FWHM
		# This factor is equal to 2 * sqrt( ln (2) )
		cFactor 		= 1.6651092223153954 
		self.width 	= Parameter( fwhm / cFactor )

	def setHeight(self, height):
		"""
		Sets the gaussian's maximum value.
		
		@param height: The new gaussian's maximum value.
		"""
		self.height 	= Parameter(height)

	def setWidth(self, width):
		"""
		Sets the gaussian's width (not the FWHM)
		
		@param width: The new gaussian's width value.
		"""
		self.width 	= Parameter(width)

#==========================================================
class Parameter:
	"""
		Class of parameters. This class is used in the fitting procedures.
	"""
	def __init__( self, value):
		"""
		Create the parameter with the given value.
		
		@param value: value to be stored.
		"""
		self.value = value

	def set( self, value):
		"""
		Replace the parameter's value with a new one.
		
		@param value: new value to be stored.
		"""
		self.value = value

	def __call__(self):
		"""
		Return the stored value.
		"""
		return self.value

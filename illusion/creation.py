"""
	    __   __    
	   (  \,/  )   
	    \_ | _/    
	    (_/ \_)  
	
	   Butterfly 
	Software System

	Illusion Data-Synthesizer for BTFI
	
	@author: Bruno Correa Quint
	@date: Mar-23-2009

	This file contains methods to create several kinds of data. Specially 2D images.

	Please, read the LICENSE file for more information about copy and distribution.

"""

from scipy import arange, ones

#==========================================================
def flat( x, y, V ):
	"""
	Create flat image.
	
	This method is used to create a single 2D flat image.
	
	@param	x: An integer value representing CCD's width.
	@param 	y: An integer value representing CCD's height.
	@param	V: A constant value for all pixels.

	"""
	data = V * ones( ( x, y ), dtype=float )
	return data
	
#==========================================================	
def xlin( x, y, a, b):
	"""
	Create a x-linear gradient
	
	This method is used to create a 2D image where its values are constant in Y direction 
	and	vary linearly accordly with the linear equation:
		
		V = a * x + b 
		
	@param x: An integer value representing CCD's width.
	@param y: An integer value representing CCD's height.
	@param a: A value that represents the angular coeficient of the equation above.
	@param b: A value that represents the linear coeficient of the equation above.
	"""
	tmpX = arange( x, dtype=float ) * a + b
	tmpY = ones( y, dtype=float  )
	return meshgrid( tmpX, tmpY )[0]
	
#==========================================================	
def ylin( x, y, c, d):
	"""
	Create a y-linear gradient
	
	This method is used to create a 2D image where its values are constant in X direction 
	and vary linearly accordly with the linear equation:
		
		V = c * y + d 
		
	@param x: An integer value representing CCD's width.
	@param y: An integer value representing CCD's height.
	@param c: A value that represents the angular coeficient of the equation above.
	@param d: A value that represents the linear coeficient of the equation above.
	"""
	tmpX = ones( x, dtype=float )
	tmpY = arange( y, dtype=float ) * c + d
	return meshgrid( tmpX, tmpY )[1]
	
#==========================================================	
def xquad( x, y, a, b, c ):
	"""
	Create a gradient in X direction following a 2nd degree polynom.
	
	This method is used to create a 2D image where it values are constant in Y direction 
	and vary in X with a 2nd degree polynom according with the function:
	
		V = a * x ** 2 + b * x + c
		
	@param x: An integer value representing CCD's width.
	@param y: An integer value representing CCD's height.
	@param a: A value that represents the quadratic term in the equation above.
	@param b: A value that represents the angular term in the equation above.
	@param c: A value that represents the linear term in the equation above.
	"""
	tmp = arange( x, dtype=float )
	tmpX = a * tmp ** 2 + b * tmp + c
	tmpY = ones( y )
	return meshgrid( tmpX, tmpY )[0]

#==========================================================	
def yquad( x, y, d, e, f ):
	"""
	Create a gradient in Y direction following a 2nd degree polynom.
	
	This method is used to create a 2D image where it values are constant in X direction 
	and vary in Y with a 2nd degree polynom according with the function:
	
		V = d * y ** 2 + e * y + f
		
	@param x: An integer value representing CCD's width.
	@param y: An integer value representing CCD's height.
	@param d: A value that represents the quadratic term in the equation above.
	@param e: A value that represents the angular term in the equation above.
	@param f: A value that represents the linear term in the equation above.
	"""
	tmp = arange( y, dtype=float )
	tmpX = ones( x, dtype=float )
	tmpY = d * tmp ** 2 + e * tmp + f
	return meshgrid( tmpX, tmpY )[1]

#==========================================================	
def flat3D( x, y, z, v, z0 ):
	"""
	Create a 3D cube with one frame 'z0' containing a even illumination of intensity 'v' 
	and all other frames with intensity 0.
	
	@param x: An integer value representing CCD's width.
	@param y: An integer value representing CCD's height.
	@param z: An integer value representing CCD's depth.
	@param v: The value that the frame will have.
	@param z0: The position in Z direction of the even illuminated frame.
	"""
	tmp = zeros( ( z, x, y ), dtype=float )
	tmp[z0] = ( ones( (x, y), dtype=float ) * v ).copy()
	return tmp

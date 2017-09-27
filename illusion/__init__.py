from __future__ import absolute_import

# .: PyFits :.
try:
    import astropy.io.fits as pyfits
except ImportError:
    print("WARNING: PyFits not found! Some features may not work.")
    pass

# .: SciPy :.
try:
    import scipy
except ImportError:
    print("WARNING: SciPy not found! Some features may not work.")
    pass

# .: PsyCO :.
try:
    import psyco
    psyco.full()
except:
    pass

from . import (auxclasses, butterfly, creation, datamanip, fpdata, gui, iodata,
    objects, version)

from .fpdata import FabryPerot, Detector
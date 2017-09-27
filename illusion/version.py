# -*- coding: utf-8 -*-
"""
v1.5.0
 Reformated the whole project. `illusion` is now a script with default values
 that can be overwritten using a config file or flags in the command line.

frozen v1.3
    - GUI: CHANGED the extentions of illusionGUI.iImage from *.fits to [*.dat,*.txt]
    - GUI: FIXED problem that created config file using only integers instead of floats.
    - ENGINE: Added the option of add poisson error while creating new cubes.

v1.4.20
    - Fixed the data cube creation from spectrum.

v0.3.23
    - Started doc of illusion.fpdata.
    - Class illusion.fpdata.Detector documentated.
    - Class illusion.fpdata.FabryPerot documentated.
    - Tests with raw cube creation done!
    - Tests with spectrum cube creation done!
    - Tests with image cube creation done!
    - Tests with dephased cube creation done!
    - Tests with spectrum convolution done!
    - Documentation on illusion.creation done!

v0.3.20
    - Testing illusion.iodata.readFits by reading a 2D and a 3D fits and
    displaying it in the screen using pylab. Ok!
    - Testing illusion.iodata.write2DPNG by reading a 2D fits with readFits and
    exporting it to PNG using all the available options.
    - Together with the *.write2DPNG method, the method
    illusion.iodata.findNewFilename was
    - Created and tested illusion.iodata.write3DPNG

v0.3.19 Module called illusion.stdfunc does not exist anymore since it was used
    to store only a gaussian function, which is already defined on
    illusion.objects. Methods already documented:
    illusion.iodata.readFits (old: illusion.iodata.readFits)
    illusion.iodata.readEmLines (old: illusion.iodata.readSpectrum) (Tested and working)
    illusion.iodata.data2png substituted by illusion.iodata.writePNG,
    illusion.iodata.write2DPNG and illusion.iodata.write3DPNG. (have to write)
    illusion.iodata.findNewFilename created to make the code cleaner when finding
        available filenames to avoid overwriting.
    For tomorrow: Test everything befor proceed

v0.3.18 Recreated method for convolution using an array and a function as arguments.
    Methods used until now used two arrays.
    Module illusion.noises does not exist anymore. The only method inside it was
    illusion.noises.poisson, which was moved to illusion.datamanip.

    Resumo dos modulos, métodos e classes modificadas/criadas:
    - illusion.datamanip.convolve1d
    - illusion.datamanip.addPoisson

v0.3.17
 Cleaning code and documentation process started
  * illusion.__init__.py: Doc done! Created tests to check available libraries.
  * illusion.butterfly.py: Done!
  * illusion.datamanip: 	New module created from illusion.fitdata and illusion.operators1D.
  These two modules will not exist anymore.
  Available methods are:
   - illusion.datamanip.index1D
   - illusion.datamanip.fit
   - illusion.datamanip.fitGaussian
   Doc done!
   * illusion.objects:
    New module created from illusion.classes and illusion.functions.
    These two modules will not exist anymore.
    Available classes are:
     - illusion.objects.Delta
     - illusion.objects.Gaussian
     - illusion.objects.Parameter
     Doc done!

v0.3.16
 Binning in unbinning now available.

v0.3.11
 Now Illusion can create cubes from a spectrum with multiple lines. It is not
 optimized yet so it takes longer time to process.

v0.3.9
 Now Illusion can extract spectrum from a region of interest instead of getting
 it only from a pixel.

v0.3.6
 First pre-release of the Illusion's Package. It still have some issues to be
 solved before a complete release. These issues are:
 - Spectrum extration from a Region of Interest.
 - Cube generation from a spectrum.
 - Add header information.
 - Check convolutions methods.
 - Check gaussian fitting methods.
 - Binnnig recovering.
"""
api = 1
feature = 5
bug = 0

month = 9
year = 2017

__str__ = 'v{:d}.{:d}.{:d} {:d}-{:0d}'.format(api, feature, bug, year, month)

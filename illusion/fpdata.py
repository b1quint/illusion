import datetime
import numpy as np

from astropy.io import fits as pyfits

from auxclasses import progressBar


class Detector:
    """
    Detector

    This class represents the detector inside the instrument. When it is
    defined, one shall give it the data-cube's dimensions, the physical pixel
    size and one can also define a binning if desired.

    Args:
        width (int): the detector's width in pixels units.
        height (int): the detector's height in pixels units.
        depth (int): the detector's depth in number of frames.
        pixel_size (float): each pixel's size in X and Y directions.
    """

    def __init__(self, width, height, depth, pixel_size):

        self.width = width
        self.height = height
        self.depth = depth
        self.pixel_size = pixel_size

        self.center = [self.width / 2, self.height / 2]
        self.data = np.zeros((self.depth, self.width, self.height), np.float32)

        self.header = None

    def get_spectrum(self, x, y):
        """
        Get the spectrum of a point or of a Region Of Interest (RoI).

        Args:
            x (int): position in X axis
            x (list): start and end position in X axis with [x0, xf]

            y (int): position in Y axis
            y (list): start and end position in Y axis with [y0, yf]
        """
        if isinstance(x, int):
            x1 = x
            x2 = x + 1
        elif isinstance(x, list):
            x1 = x[0]
            x2 = x[1]
        else:
            raise ValueError('x is not an integer nor a list')

        if isinstance(y, int):
            y1 = y
            y2 = y + 1
        elif isinstance(y, list):
            y1 = y[0]
            y2 = y[1]
        else:
            raise ValueError('y is not an integer nor a list')

        spec = self.data[:, x1:x2, y1:y2]
        spec = np.sum(spec, axis=[1, 2])

        return spec

    def set_center(self, x, y):
        """
        Set center

        This method is used to set the Fabry-Perot rings' center.

        Args:
            x (float): position in X axis
            y (float): position in Y axis

        """
        self.center = [x, y]

    def set_header(self, fp, header=None):
        """
        Add information about the created data to a header.

        Args:
            fp (illusion.FabryPerot): a FabryPerot object which was used for the
             data creation. It contains general information that will be added
             to the header.

            header (astropy.io.fits.Header): the header where the information
            will be added. Default is None.

        """
        now = datetime.datetime.now()

        if header is None:
            h = pyfits.Header()
        else:
            h = header

        h.add_blank(" ")
        h.add_blank(" __   __  ")
        h.add_blank("(  \,/  ) Data created using:")
        h.add_blank(" \_ | _/  Butterfly Software System for BTFI")
        h.add_blank(" (_/ \_)  Illusion Data-Synthesizer Package v1.4.23")
        h.add_blank(" ")

        # FP info
        h.update("WLENGTH", fp.centralWavelength, "Central Wavelength [um]")
        h.update("SPECR", fp.resolvingPower, "Spectral Resolution")
        h.update("FINESSE", fp.finesse, "The Fabry-Peror Finesse")
        h.update("StartGV", fp.GStart, "Start gap value [um]")
        h.update("StepGV", round(fp.GStep * 1e3, 2), "Gap step size [nm]")
        h.update("REFIND", fp.refractiveIndex, "Refractive index withing gap")
        h.update("ORDER", fp.order, "Interference order")
        h.update("XCENTER", self.center[0], "X coordinate of the rings' center")
        h.update("YCENTER", self.center[1], "Y coordinate of the rings' center")
        h.update("FLENGTH", fp.focalLength * 1e-3, "Focal length [mm]")

        # CCD Info
        h.update("WIDTH", self.width, "Cube's width in pixels")
        h.update("HEIGHT", self.height, "Cube's height in pixels")
        h.update("DEPTH", self.depth, "Cube's depth in numer of frames")
        h.update("PIXSIZE", self.pixel_size, "Physical pixel size [um]")

        # MORE Info
        h.update("DATE", "%d-%d-%d" % (now.year, now.month, now.day),
                 "FITS birthsday")
        h.update("HOUR", "%d:%d" % (now.hour, now.minute), "FITS birthstime")

        h.add_blank("--- Fabry Perot's data ---", before='WLENGTH')
        h.add_blank("--- Detector's data ---", before='WIDTH')
        h.add_blank("--- More info ---", before='DATE')


class FabryPerot:
    """
    Fabry-Perot

    This class holds all the physical information about the instrument necessary
    to use in the Airy's Function (the one that describes the FP rings).

    Args:
        central_wavelength (float):
            the wavelength that will appear in the central pixel in the first
            frame of the data cube. It is used to derive the other FP parameters
            [microns].

        resolution (float):
            the spectral resolving power of the Fabry-Perot.

        finesse (float):
            the Fabry-Perot's Finesse.

        focal_length (float):
            the camera's focal length [microns].

        refractive_index (float):
            the refractive index in the Fabry-Perot's gap. The default value is
            1 (air).

        extrapolate (float):
            this key argument is used in the case that one desires to get more
            or less than a free-specral-range, e.g., if we want a 20% deeper
            cube, extrapolate will be 1.2.
    """
    def __init__(self, central_wavelength, resolution, finesse, focal_length,
                 refractive_index=1.0, extrapolate=1.0, verbose=False):

        self.central_wavelength = central_wavelength
        self.spectral_resolution = resolution
        self.finesse = finesse
        self.refractive_index = refractive_index
        self.focal_length = focal_length

        self.order = self.spectral_resolution / self.finesse
        self.w_fsr = self.central_wavelength / self.order
        self.z_fsr = self.central_wavelength / 2.
        self.gap_size = \
            self.order * self.central_wavelength / self.refractive_index / 2

        self.n_points = int(2 * self.finesse)

        self.g_start = self.gap_size
        self.g_stop = self.gap_size + self.z_fsr
        self.g_step = self.z_fsr / (2 * self.finesse)

        self.w_start = self.central_wavelength
        self.w_stop = self.central_wavelength + self.w_fsr
        self.w_step = self.w_fsr / (2 * self.finesse)

        self.verbose = verbose
        self.n_points = int(self.n_points * extrapolate)

    def raw_cube(self, ccd, observed_wavelength=None, intensity=1.0,
                 noise=None):
        """
        Create what is called a Raw Cube on Illusion's context.
        This kind of data cube is generated by a monochromatic even
        illuminated screen. It is the simplest case of Fabry-Perot. It is
        calculated using the maximum value as 1.

        Args:
            ccd (illusion.Detector):
                contains information about the instrument's detector.

            intensity (float):
                Constant intensity of the source's.

            observed_wavelength (float):
                the source's wavelength in microns.

            noise (function):
                A function which returns the data with the noise already
                included.
        """

        # Fabry Perot Dictionary
        N = self.finesse
        n = self.refractive_index
        w = self.central_wavelength
        L = self.g_start

        # Calc the center of the rings
        x0 = ccd.center[0] * ccd.pixelSize
        y0 = ccd.center[1] * ccd.pixelSize

        # Verbose information
        v, ii, iMax = self.verbose, 0, ccd.data.shape[0]

        # Default Values
        noise = lambda x: x
        i0 = 100.

        if noise:
            noise = np.poisson

        # Options
        i0 = intensity

        if observed_wavelength is not None:
            w = observed_wavelength

        if noise is None:
            noise = lambda x: x

        # Creating the cube

        x = np.arange(ccd.data.shape[2])
        y = np.arange(ccd.data.shape[1])
        Y, X = np.meshgrid(x, y)
        R = np.sqrt((X - x0) ** 2 + (Y - y0) ** 2)
        T = np.arctan(R / self.focal_length)

        for k in range(ccd.data.shape[0]):
            tmp = 2 * N / np.pi * np.sin(2 * np.pi * L * n * np.cos(T) / w)
            tmp2 = i0 / (1 + tmp ** 2)
            ccd.data[k] = noise(tmp2)
            if v:
                progressBar(ii, iMax, 20)
                ii += 1
            L += self.g_step

        if v:
            progressBar(iMax, iMax, 20)


    def specCube(self, ccd, spec, **kwargs):
        """
        Create what is called a Spectrum Cube on Illusion's context. This kind of
        cube is created from a even illuminated screed with several emission lines.
        It is calculated using the lines' intensity as their maximum value.

        @param ccd: a Detector object which contains information about the instrument's
        detector and where the data will be stored.
        @param spec: a single spectrum. One has to take care with this parameter because
        in practice, this method calculates a whole cube for each point given. So, this method
        is more useful to reproduce calibration cubes.
        @kwarg noise: if True, add poisson noise to the cube
                      (see numpy.random.poisson for more info).
        """

        # First we free some space in memory
        ccd.data = zeros_like(ccd.data)

        # Fabry Perot Dictionary
        N = self.finesse
        n = self.refractive_index

        # Calc the center of the rings
        x0 = ccd.center[0] * ccd.pixelSize
        y0 = ccd.center[1] * ccd.pixelSize

        # Verbose information
        v, ii, iMax = self.verbose, 0, (ccd.data.shape[0] * spec.shape[0])

        # Options
        for key in kwargs:
            # A noisy cube?
            if (key == 'noise'):
                if kwargs[key]:
                    noise = poisson
                else:
                    noise = lambda x: x

        # Creating the cube
        for s in range(spec.shape[0]):
            L = self.g_start
            for k in range(ccd.data.shape[0]):
                w = spec[s, 0]
                i0 = spec[s, 1]
                for i in range(ccd.data.shape[2]):
                    for j in range(ccd.data.shape[1]):
                        x = i * ccd.pixelSize
                        y = j * ccd.pixelSize
                        r = sqrt((x - x0) ** 2 + (y - y0) ** 2)
                        t = atan(r / self.focal_length)
                        tmp = 2 * N / pi * sin(2 * pi * L * n * cos(t) / w)
                        tmp2 = i0 / (1 + tmp ** 2)
                        ccd.data[k][i][j] += noise(tmp2)
                if v: progressBar(ii, iMax, 20)
                ii += 1
                L += self.g_step

        if v: progressBar(iMax, iMax, 20)

    # ==================================================
    def imageCube(self, ccd, iframe, wLength, **kwargs):
        """
        Create a data cube using an image as input. It is like we have an
        object at infinity. The wavelength have to be given. This is the
        wavelength corresponding to the image.

        @param ccd: a Detector object which contains information about the
        instrument's detector and where the data will be stored.
        @param iframe: a single frame containg the the spacial information.
        @param wLength: the source's wavelength in microns.
        @kwargs noise: if True, add poisson noise to the cube
        (see numpy.random.poisson for more info).
        """
        # First we free some space in memory
        ccd.data = zeros_like(ccd.data)

        # Are both at the same size?
        if not (ccd.data.shape[1:] == iframe.shape):
            print "CCD DIM: ", ccd.data.shape[1:]
            print "FRAME DIM:", iframe.shape
            raise TypeError, "Input image and CCD do not have same dimensions."

        # Fabry Perot Dictionary
        N = self.finesse
        n = self.refractive_index
        w = wLength
        L = self.g_start

        # Calc the center of the rings
        x0 = ccd.center[0] * ccd.pixelSize
        y0 = ccd.center[1] * ccd.pixelSize

        # Verbose information
        v, ii, iMax = self.verbose, 0, ccd.data.shape[0]
        ccd.data = zeros_like(ccd.data)

        # Options
        for key in kwargs:
            # A noisy cube?
            if (key == 'noise'):
                if kwargs[key]:
                    noise = poisson
                else:
                    noise = lambda x: x

        # Creating the cube
        for k in range(ccd.data.shape[0]):
            for i in range(ccd.data.shape[2]):
                for j in range(ccd.data.shape[1]):
                    x = i * ccd.pixelSize
                    y = j * ccd.pixelSize
                    r = sqrt((x - x0) ** 2 + (y - y0) ** 2)
                    t = atan(r / self.focal_length)
                    tmp = 2 * N / pi * sin(2 * pi * L * n * cos(t) / w)
                    tmp2 = iframe[j][i] / (1 + tmp ** 2)
                    ccd.data[k][j][i] = noise(tmp2)
            if v: progressBar(ii, iMax, 20)
            ii += 1
            L += self.g_step
        if v: progressBar(iMax, iMax, 20)

    def dephasedCube(self, ccd, icube, ipos=None):
        """
        This method is used to invert the process of phase correction, i.e.,
        from a phase corrected Data Cube it created what is called in the
        Illusion's context of Dephased Cube.

        Args:

            ccd (illusion.Detector): contains information about the instrument's
            detector and where the data will be stored.

            icube (numpy.ndarray): the phase corrected Data Cube that will
            be used to generate the dephased cube. It has to have the same size
            in pixel units that the output cube or else this method will do the
            dephase process only in part of the original cube.

            ipos () : ???
        """
        if ipos is None:
            ipos = []

        ccd.data = zeros_like(ccd.data)

        N = self.finesse
        n = self.refractive_index
        w = self.w_start

        x0 = ccd.center[0] * ccd.pixelSize
        y0 = ccd.center[1] * ccd.pixelSize

        ii = 0
        iMax = ccd.data.shape[0] * iCube.shape[0]

        if not ipos:
            count = 0
            for s in range(icube.shape[0]):
                ipos.append(count)
                count += 1

        for s in range(icube.shape[0]):
            L = self.g_start + ipos[s]
            for k in range(ccd.data.shape[0]):
                # print "Scan number: ", s, "Frame number: ", k, "Original frame at: ", ipos[s]
                for i in range(ccd.data.shape[2]):
                    for j in range(ccd.data.shape[1]):
                        x = i * ccd.pixelSize
                        y = j * ccd.pixelSize
                        r = sqrt((x - x0) ** 2 + (y - y0) ** 2)
                        t = atan(r / self.focal_length)
                        tmp = 2 * N / pi * sin(2 * pi * L * n * cos(t) / w)
                        ccd.data[k][i][j] += icube[s][i][j] / (1 + tmp ** 2)
                progressBar(ii, iMax, 20)
                ii += 1
                L += self.g_step
            w += self.w_step
        progressBar(iMax, iMax, 20)

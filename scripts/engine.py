"""
# ===========================================================================
# Illusion Engine v1.0
#
# by Bruno Quint, Jan 2010
# ---------------------------------------------------------------------------
# MAIN FILE
# ===========================================================================
"""

import sys
import illusion

if __name__ == '__main__':

    obsconfigfile = './Conf/obs_conf.py'
    engconfigfile = './Conf/eng_conf.py'

    if len(sys.argv) > 1:
        obsconfigfile = sys.argv[1]
        if len(sys.argv) > 2:
            engconfigfile = sys.argv[2]
        else:
            engconfigfile = './Conf/eng_conf.py'
    else:
        obsconfigfile = './Conf/obs_conf.py'
        engconfigfile = './Conf/eng_conf.py'

    try:
        execfile(engconfigfile)
    except IOError:
        class EConfig:
            pass
        EConfig.verbose = True
        EConfig.overwrite = True

    if EConfig.verbose: print  __doc__

    if EConfig.verbose: print '# Reading user config file...'
    try:
        execfile(obsconfigfile)
        if EConfig.verbose: print '# Success!'
        if EConfig.verbose: print '# %s file opened!' % obsconfigfile
    except IOError:
        if EConfig.verbose: print '# Failed!'
        if EConfig.verbose: print '# %s file not found!' % obsconfigfile
        if EConfig.verbose: print '# Leaving the engine.'
        exit()

    fp = illusion.fpdata.FabryPerot( Config.lambda_0 * 1e-3,
                                     Config.specResolution,
                                     Config.finesse,
                                     Config.focalLength * 1e3,
                                     extrapolate = Config.extrapolate,
                                     verbose = EConfig.verbose)

    ccd = illusion.fpdata.Detector(Config.width / Config.binning,
                                   Config.height / Config.binning,
                                   fp.n_points,
                                   Config.pixelSize * Config.binning)
    Config.output = Config.output


    if Config.type == 'raw':
        if EConfig.verbose: print '# Creating raw data-cube...'
        fp.raw_cube(ccd, observed_wavelength=Config.input_wavelength * 1e-3, noise=Config.noise)
        ccd.set_header(fp)
        illusion.iodata.writeFits(Config.output, ccd.data, ccd.header,
        overwrite=EConfig.overwrite, verbose=EConfig.verbose)
        if EConfig.verbose: print '# Done!\n'

    elif Config.type == 'image':
        if EConfig.verbose: print '# Reading image fits...'
        try:
            rawImage = illusion.iodata.getdata( Config.input_image )
        except IOError:
            print '# Failed reading %s file. Leaving program now. \n' % Config.input_image
            exit()
        if EConfig.verbose: print '# Creating image data-cube...'
        fp.imageCube(ccd, rawImage, Config.input_wavelength * 1e-3, noise=Config.noise)
        ccd.set_header(fp)
        illusion.iodata.writeFits(Config.output, ccd.data, ccd.header,
        overwrite=EConfig.overwrite, verbose=EConfig.verbose)
        if EConfig.verbose: print '# Done!\n'


    elif Config.type == 'spectrum':
        if EConfig.verbose: print '# Reading spectrum file...'
        spec = illusion.iodata.readEmLines(Config.input_spectrum)
        spec[:,0] *= 1e-3
        if EConfig.verbose: print '# Creating spectrum data-cube...'
        fp.specCube(ccd,spec, noise=Config.noise)
        ccd.set_header(fp)
        illusion.iodata.writeFits(Config.output, ccd.data, ccd.header,
        overwrite=EConfig.overwrite, verbose=EConfig.verbose)
        if EConfig.verbose: print '# Done!\n'

### END OF FILE ###

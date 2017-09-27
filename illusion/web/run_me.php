<!--
#=============================================================================
# Illusion Web Server v1.0
#
# by Bruno Quint, Jan 2010
#-----------------------------------------------------------------------------
# This file is part of the package called Illusion. Please, read LICENSE.txt
# file for information about copyrights.
#-----------------------------------------------------------------------------
# This file contains all the actions that shall be performed once 'submit'
# button is pressed.
#=============================================================================
-->

<!-- Run Me! ---------------------------------------------------------------->
<?php
    function parseNumber($num_arg)
    {
        if (is_numeric($num_arg))
            return $num_arg;
        else
            die("$num_arg is not a number!");
    }
?>

<?php

    $path_to_illusion = "/home/bquint/Work/BTFI/Illusion/Frozen/v1_1/Engine/engine.py";
    
    $my_string = "";
    $my_string = $my_string . "class Config:\n";
    $my_string = $my_string . "    pass\n";
    $my_string = $my_string . "\nConfig.type = '$_POST[type]'";
    $my_string = $my_string . "\n\nConfig.lambda_0 = "
                            . parseNumber($_POST[wlCentral]);
    $my_string = $my_string . "\nConfig.specResolution = "
                            . parseNumber($_POST[specResolution]);
    $my_string = $my_string . "\nConfig.finesse = "
                            . parseNumber($_POST[finesse]);
    $my_string = $my_string . "\nConfig.focalLength = "
                            . parseNumber($_POST[focal_length]);
    $my_string = $my_string . "\nConfig.extrapolate = "
                            . (parseNumber($_POST[extrapolate]) / 100);
    $my_string = $my_string . "\n\nConfig.width = "
                            . parseNumber($_POST[width]);
    $my_string = $my_string . "\nConfig.height = "
                            . parseNumber($_POST[height]);
    $my_string = $my_string . "\nConfig.pixelSize = "
                            . parseNumber($_POST[pixel_size]);
    $my_string = $my_string . "\nConfig.binning = "
                            . parseNumber($_POST[binning]);
    $my_string = $my_string . "\n\nConfig.output = "
                            . "'./temp_output.fits'";
    $my_string = $my_string . "\nConfig.input_wavelength = "
                            . parseNumber($_POST[wlSource]);
    $my_string = $my_string . "\nConfig.input_image = "
                            . "'./temp_image.fits'";
    $my_string = $my_string . "\nConfig.input_spectrum = "
                            . "'./temp_spectrum.txt'";
    $my_string = $my_string . "\n\nEConfig.verbose = True"; 
    $my_string = $my_string . "\nEConfig.overwrite = True";    
    
    /* This was an attempt to read a template of the config file parsing the
       values into it. */
    /*
    $filename = "stdcfg.txt";
    $fd = fopen($filename, "r") or die("Can't open file $filename");
    $my_string = "" . fread($fd, filesize($filename));
    */
    
    print("<pre>$my_string</pre>");
    
    /* File handling */
    $filename = "temp_config.py";
    $fd = fopen($filename, "w") or die("Can't open file $filename");
    $fout = fwrite($fd, $my_string);
    fclose($fd);
    
    /* Running Illusion Engine */
    system("python $path_to_illusion temp_config.py");
    system("ls *.fits");
    
?>
<!--------------------------------------------------------------------------->
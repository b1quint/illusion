<!--
#=============================================================================
# Illusion Web Server v1.0
#
# by Bruno Quint, Jan 2010
#-----------------------------------------------------------------------------
# This file is part of the package called Illusion. Please, read LICENSE.txt
# file for information about copyrights.
#=============================================================================
-->

<?php include("./illusion/Web/index.php"); ?>

<html>
    <head>
        <title> BQ's Page </title>
        <style type="text/css"> <!--
            body {font-family: sans-serif; font-size: 12pt;}
            h1 {font-size: 16pt; text-align: left}
            div.gray {color: #999999}
        --> </style>
    </head>
        
    <?php include("colors.inc"); ?>
    <?php
        // include("variables.inc");
        // $my_config = new Config;
    ?>

    <body>
        <table cellpadding=0 width=100%>
            <tr><?php include("header.inc") ?></tr>
            <tr>
                <?php include("menu.inc") ?>
                <?php include("illusion_gui.php") ?>
            </tr>
        </table>
    </body>
</html>
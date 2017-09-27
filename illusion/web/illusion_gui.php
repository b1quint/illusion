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

<td bgcolor="<?php print("$White"); ?>" width=80%>
    <form method="post" action="run_me.php"><table cellpadding=20>
        <tr>
            <?php include("fabryperot.php");
                  include("detector.inc"); ?>
        </tr>
        <tr>
            <?php include("types.php");
                  include("io.php"); ?>
        </tr>
        <tr><td align="right" colspan="2"><input type="submit"></td></tr>
    </table></form>
</td>
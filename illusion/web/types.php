<!--
#=============================================================================
# Illusion Web Server v1.0
#
# by Bruno Quint, Jan 2010
#-----------------------------------------------------------------------------
# This file is part of the package called Illusion. Please, read LICENSE.txt
# file for information about copyrights.
#-----------------------------------------------------------------------------
# This file holds the graphical interface that will store the information
# regarding to the type of cubes that are available.
#=============================================================================
-->   

<!-- Cube type -------------------------------------------------------------->
<td valign="top"><table>

    <tr><td colspan="2"><b>Cube Type</b></td></tr>
    
    <tr><td>
        <input type="radio"
               name="type"
               value="raw"
               checked="checked">
        Raw cube</td></tr>
    
    <tr><td><div class="gray">
        <input type="radio"
               name="type"
               value="image"
               disabled="disabled">
        Image cube</div></td></tr>
    
    <tr><td><div class="gray">
        <input type="radio"
               name="type"
               value="spectrum"
               disabled="disabled">
        Spectrum cube</div></td></tr>

</table></td>
<!--------------------------------------------------------------------------->
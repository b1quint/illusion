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
# regarding to the Fabry-Perot itself. 
#=============================================================================
-->

<!---------------------- Fabry Perot Parameters ----------------------------->
<td valign="top"><table>

    <tr><td colspan="2"><b>Fabry Perot</b></td></tr>
    
    <tr><td align="left">Central Wavelength:</td>
        <td align="right">
        <input type="text" name="wlCentral" size=5 value="500" ></td>
        <td align="left">microns</td></tr>
            
    <tr><td align="left">Spectral Resolution:</td>
        <td align="right">
        <input type="text" name="specResolution" size=5 value="20000">
        </td></tr>
            
    <tr><td align="left">Finesse:</td>
        <td align="right">
        <input type="text" name="finesse" size=5 value="25">
        </td></tr>
            
    <tr><td align="left">Extrapolate:</td>
        <td align="right">
        <input type="text" name="extrapolate" size=5 value="110"></td>
        <td align="left">%</td></td>
            
    <tr><td align="left">Focal length:</td>
        <td align="right">
        <input type="text" name="focal_length" size=5 value="350"></td>
        <td align="left">mm</td></tr>

</table></td>
<!--------------------------------------------------------------------------->
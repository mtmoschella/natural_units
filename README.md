<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module natural_units</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>natural_units</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:/vanya/matthew/Dropbox/Princeton/phys/code/natural_units/natural_units.py">/vanya/matthew/Dropbox/Princeton/phys/code/natural_units/natural_units.py</a></font></td></tr></table>
    <p><tt>A&nbsp;simple&nbsp;natural&nbsp;units&nbsp;conversion&nbsp;package.<br>
&nbsp;<br>
This&nbsp;module&nbsp;is&nbsp;used&nbsp;for&nbsp;converting&nbsp;(astropy)&nbsp;units&nbsp;from&nbsp;physical&nbsp;units<br>
to&nbsp;natural&nbsp;units&nbsp;where&nbsp;$\hbar=c=1$,&nbsp;with&nbsp;the&nbsp;convention&nbsp;that&nbsp;the&nbsp;unique<br>
remaining&nbsp;'natural'&nbsp;dimension&nbsp;is&nbsp;energy&nbsp;(eV&nbsp;by&nbsp;default).<br>
This&nbsp;module&nbsp;also&nbsp;contains&nbsp;useful&nbsp;constants&nbsp;in&nbsp;physical&nbsp;astropy&nbsp;units,<br>
specifically:&nbsp;mpl,&nbsp;c,&nbsp;habar,&nbsp;G,&nbsp;eps0</tt></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#aa55cc">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Modules</strong></big></font></td></tr>
    
<tr><td bgcolor="#aa55cc"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><table width="100%" summary="list"><tr><td width="25%" valign=top><a href="numpy.html">numpy</a><br>
</td><td width="25%" valign=top><a href="astropy.units.html">astropy.units</a><br>
</td><td width="25%" valign=top></td><td width="25%" valign=top></td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#eeaa77">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Functions</strong></big></font></td></tr>
    
<tr><td bgcolor="#eeaa77"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl><dt><a name="-convert"><strong>convert</strong></a>(x, unit, verbose=False)</dt><dd><tt>convenient&nbsp;alias&nbsp;for&nbsp;fromNaturalUnits</tt></dd></dl>
 <dl><dt><a name="-fromNaturalUnits"><strong>fromNaturalUnits</strong></a>(x, output_unit, verbose=False)</dt><dd><tt>Returns&nbsp;the&nbsp;given&nbsp;(natural&nbsp;or&nbsp;physical)&nbsp;astropy&nbsp;Quantity&nbsp;in&nbsp;the&nbsp;physical&nbsp;units&nbsp;specified&nbsp;by&nbsp;output_unit<br>
&nbsp;<br>
x:&nbsp;an&nbsp;astropy&nbsp;Quantity&nbsp;or&nbsp;Unit<br>
&nbsp;<br>
output_unit:&nbsp;an&nbsp;astropy&nbsp;UnitBase<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;must&nbsp;be&nbsp;naturally&nbsp;compatible&nbsp;with&nbsp;&lt;x&gt;&nbsp;or&nbsp;will&nbsp;raise&nbsp;AssertionError</tt></dd></dl>
 <dl><dt><a name="-toNaturalUnits"><strong>toNaturalUnits</strong></a>(x, output_unit=Unit("eV"), verbose=False)</dt><dd><tt>Returns&nbsp;the&nbsp;given&nbsp;physical&nbsp;astropy&nbsp;Quantity&nbsp;in&nbsp;the&nbsp;natural&nbsp;units&nbsp;specified&nbsp;by&nbsp;output_unit.<br>
&nbsp;<br>
x:&nbsp;an&nbsp;astropy&nbsp;Quantity&nbsp;or&nbsp;Unit<br>
&nbsp;&nbsp;&nbsp;&lt;x&gt;&nbsp;may&nbsp;be&nbsp;an&nbsp;array&nbsp;of&nbsp;values,&nbsp;but&nbsp;&lt;x&gt;&nbsp;cannot&nbsp;be&nbsp;a&nbsp;list&nbsp;of&nbsp;quantities<br>
&nbsp;&nbsp;&nbsp;i.e.&nbsp;[1.,&nbsp;2.0]*u.cm&nbsp;(ALLOWED)&nbsp;but&nbsp;[1.0*u.cm,&nbsp;2.0*u.cm]&nbsp;(NOT&nbsp;ALLOWED)<br>
&nbsp;<br>
output_unit:&nbsp;an&nbsp;astropy&nbsp;UnitBase&nbsp;of&nbsp;physical_type&nbsp;'energy'<br>
&nbsp;<br>
verbose:&nbsp;(optional)&nbsp;boolean,&nbsp;run&nbsp;in&nbsp;verbose&nbsp;mode</tt></dd></dl>
</td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#55aa55">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Data</strong></big></font></td></tr>
    
<tr><td bgcolor="#55aa55"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><strong>G</strong> = &lt;&lt;class 'astropy.constants.codata2018.CODATA2018...e-15 unit='m3 / (kg s2)' reference='CODATA 2018'&gt;<br>
<strong>c</strong> = &lt;&lt;class 'astropy.constants.codata2018.CODATA2018...rtainty=0.0 unit='m / s' reference='CODATA 2018'&gt;<br>
<strong>eps0</strong> = &lt;&lt;class 'astropy.constants.codata2018.EMCODATA20...nty=1.3e-21 unit='F / m' reference='CODATA 2018'&gt;<br>
<strong>hbar</strong> = &lt;&lt;class 'astropy.constants.codata2018.CODATA2018...certainty=0.0 unit='J s' reference='CODATA 2018'&gt;<br>
<strong>mpl</strong> = &lt;Quantity 2.17643434e-08 J(1/2) kg(1/2) s / m&gt;</td></tr></table>
</body></html>
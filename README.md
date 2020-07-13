# natural_units module

A simple natural units conversion package.

This module is used for converting (astropy) units from physical units
to natural units where $hbar=c=1$, with the convention that the unique
remaining ‘natural’ dimension is energy (eV by default).
This module also contains useful constants in physical astropy units,
specifically: mpl, c, habar, G, eps0


### natural_units.convert(x, unit, verbose=False)
convenient alias for fromNaturalUnits


### natural_units.fromNaturalUnits(x, output_unit, verbose=False)
Returns the given (natural or physical) astropy Quantity in the physical units specified by output_unit

x: an astropy Quantity or Unit

output_unit: an astropy UnitBase

    must be naturally compatible with <x> or will raise AssertionError


### natural_units.toNaturalUnits(x, output_unit=Unit('eV'), verbose=False)
Returns the given physical astropy Quantity in the natural units specified by output_unit.

x: an astropy Quantity or Unit

    <x> may be an array of values, but <x> cannot be a list of quantities
    i.e. [1., 2.0]\*u.cm (ALLOWED) but [1.0\*u.cm, 2.0\*u.cm] (NOT ALLOWED)

output_unit: an astropy UnitBase of physical_type ‘energy’

verbose: (optional) boolean, run in verbose mode

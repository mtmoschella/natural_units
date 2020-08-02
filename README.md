# Python Module: natural_units.py
A simple natural units conversion package for `astropy` python.

This module is used for converting (astropy) units from physical units
to natural units where $\hbar=c=1$, with the convention that the unique
remaining 'natural' dimension is energy (eV by default).
This module also contains useful constants in physical astropy units,
specifically: `mpl`, `c`, `hbar`, `G`, `eps0`

## Modules
- `numpy`
- `astropy.units`

## Functions

### toNaturalUnits(x, output_unit=Unit("eV"), verbose=False)
Returns the given (natural or physical) astropy Quantity in the physical units specified by `output_unit`
- `x`: an astropy Quantity or Unit
  - NOTE: `x` may be an array of values, but cannot be a list of astropy Quantity. For example, `numpy.array([1,2])*astropy.units.cm` is allowed, but `[1*astropy.units.cm, 2*astropy.units.cm]` is NOT ALLOWED 
- `output_unit`: (optional) an astropy Unit Base of `physical_type=='energy'`
- `verbose`: (optional) boolean, run in verbose mode

### fromNaturalUnits(x, output_unit, value=False, verbose=False)
Returns the given (natural or physical) astropy Quantity in the physical units specified by `output_unit`
- `x`: an astropy Quantity or Unit
  - NOTE: `x` may be an array of values, but cannot be a list of astropy Quantity. For example, `numpy.array([1,2])*astropy.units.cm` is allowed, but `[1*astropy.units.cm, 2*astropy.units.cm]` is NOT ALLOWED 
- `output_unit`: an astropy Unit Base. Must be compatible with `x` or will raise AssertionError
- `value`: a boolean. If False, returns an astropy Quantity in the units specified by `output_unit`. If True, returns a python scalar with value in `output_unit`, i.e. calls astropy.to_value(`output_unit`).
- `verbose`: (optional) boolean, run in verbose mode

### convert(x, unit, value=False, verbose=False)
convenient alias for `fromNaturalUnits`

## Constants
- `G`: Gravitational constant, equivalent to `astropy.constants.G`
- `c`: Speed of light, equivalent to `astropy.constants.c`
- `hbar`: (reduced) Planck constant, equivalent to `astropy.constants.hbar`
- `eps0`: Vacuum permittivity, equivalent to `astropy.constants.eps0`
- `mpl`: Planck mass, equivalent to `sqrt(hbar*c/G)`

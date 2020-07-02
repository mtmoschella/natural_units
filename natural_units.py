"""
A simple natural units conversion package.

This module is used for converting (astropy) units from physical units
to natural units where $\hbar=c=1$, with the convention that the unique
remaining 'natural' dimension is energy (eV by default).
This module also contains useful constants in physical astropy units,
specifically: mpl, c, habar, G, eps0
"""
import numpy as np
import astropy.units as u
from astropy.constants import c, hbar, G, eps0

mpl = np.sqrt(hbar*c/G) # astropy quantity


def toNaturalUnits(x, output_unit=u.eV, verbose=False):
    """
    Returns the given physical astropy Quantity in the natural units specified by output_unit.

    x: an astropy Quantity or Unit
       <x> may be an array of values, but <x> cannot be a list of quantities
       i.e. [1., 2.0]*u.cm (ALLOWED) but [1.0*u.cm, 2.0*u.cm] (NOT ALLOWED)

    output_unit: an astropy UnitBase of physical_type 'energy'

    verbose: (optional) boolean, run in verbose mode
    """
    if not isinstance(x, u.Quantity):
        if isinstance(x, u.UnitBase):
            if verbose:
                print("WARNING: converting astropy unit to quantity by multiplying by 1.0")
            x *= 1.0
        else:
            raise Exception("ERROR: x must be either an astropy quantity or unit")
    assert isinstance(output_unit, u.UnitBase), "ERROR: output_unit must be a astropy unit"

    
    assert output_unit.physical_type=='energy', "ERROR: output_unit must be a unit of energy"
    unit = x.unit.decompose() # decompose into SI units (astropy default)
    bases = unit.bases 
    powers = unit.powers
    if set(bases)<=set([u.kg, u.m, u.s, u.A]): # (SI = MKS + Ampere)
        # get dimensions of kg, m, s, A units
        if u.kg in bases:
            i = powers[bases.index(u.kg)]
        else:
            i = 0
        if u.m in bases:
            j = powers[bases.index(u.m)]
        else:
            j = 0
        if u.s in bases:
            k = powers[bases.index(u.s)]
        else:
            k = 0
        if u.A in bases:
            l = powers[bases.index(u.A)]
        else:
            l = 0

        # convert to dimensions of hbar, c, eV, eps0 units
        # this comes from analytically solving the linear system of equations that you get from preserving dimensionality
        hbar_dim = j + k - 0.5*l
        c_dim = j - 2*i + 0.5*l
        E_dim = i - j - k + l
        eps0_dim = 0.5*l
        
        return (x/((hbar**hbar_dim)*(c**c_dim)*(eps0**eps0_dim))).to(output_unit**E_dim)

    else:
        raise Exception("ERROR: can only convert to natural units if MKS+A quantity")
    return 1.0

def fromNaturalUnits(x, output_unit, verbose=False):
    """
    Returns the given (natural or physical) astropy Quantity in the physical units specified by output_unit

    x: an astropy Quantity or Unit

    output_unit: an astropy UnitBase
                 must be naturally compatible with <x> or will raise AssertionError
    """

    if not isinstance(x, u.Quantity):
        if isinstance(x, u.UnitBase):
            if verbose:
                print("WARNING: converting astropy unit to quantity by multiplying by 1.0")
            x *= 1.0
        else:
            print("WARNING: converting ordinary scalar to an astropy dimensionless quantity")
            x *= u.dimensionless_unscaled
    assert isinstance(output_unit, u.UnitBase), "ERROR: output_unit must be a astropy unit"

    x = toNaturalUnits(x) # outputs in eV**n by default
    
    natunit = x.unit.decompose()
    natbases = natunit.bases
    natpowers = natunit.powers
    check_units = True
    
    unit = output_unit.decompose() # docompose into SI units (astropy default)
    bases = unit.bases
    powers = unit.powers
    
    if set(bases)<=set([u.kg, u.m, u.s, u.A]):
        # get dimensions of kg, m, s, A units
        if u.kg in bases:
            i = powers[bases.index(u.kg)]
        else:
            i = 0
        if u.m in bases:
            j = powers[bases.index(u.m)]
        else:
            j = 0
        if u.s in bases:
            k = powers[bases.index(u.s)]
        else:
            k = 0
        if u.A in bases:
            l = powers[bases.index(u.A)]
        else:
            l = 0

        # convert to dimensions of hbar, c, eV units
        # this comes from analytically solving the linear system of equations that you get from preserving dimensionality
        hbar_dim = j + k - 0.5*l
        c_dim = j - 2*i + 0.5*l
        E_dim = i - j - k + l
        eps0_dim = 0.5*l

        if check_units:
            # make sure that dim(x)==(energy)**E_dim
            # if not, then the specified output unit is not compatible
            if set(natbases)==set([]):
                # natunit is dimensionless
                assert E_dim==0.0, "ERROR: specified output_unit is not compatible with energy dimension 0"
            else:
                assert set(natbases)==set([u.kg, u.m, u.s]), "ERROR: natural units must be (energy)**n"
                kg_power = natpowers[natbases.index(u.kg)]
                m_power = natpowers[natbases.index(u.m)]
                s_power = natpowers[natbases.index(u.s)]
                assert kg_power==E_dim and m_power==2.0*E_dim and s_power==-2.0*E_dim, "ERROR: specified output_unit is not compatible with with energy dimension "+str(kg_power)

        return (x*hbar**hbar_dim*c**c_dim*eps0**eps0_dim).to(output_unit)
    else:
        raise Exception("ERROR: can only convert to natural units if MKS+A quantity")
        

if __name__=='__main__':
    # use for testing
    pass

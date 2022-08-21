#This file contains some commonly used physical constants in the book
def Boltzmann():
    #Returns the Boltzmann constant
    return 1.380649*10**-23

def LightSpeed():
    #Returns the speed of light
    return 2.99792458*10**8

def Planck_bar():
    from math import pi
    #Returns normalized Planck's constant
    return (6.62607015*10**-34)/(2*pi)

def Planck():
    from math import pi
    #Returns normalized Planck's constant
    return (6.62607015*10**-34)

def Newton_Gravity():
    #Returns Newton's Gravitational constant
    return 6.674*10**-11

def free_space_permittivity():
    #Returns the electric permittivity of free space
    return 8.85418782*10**-12

def electron_charge():
    #Returns charge of electron in Coloumbs
    return -1.6022*1e-19

def electron_mass():
    #Returns the mass of the electron in kg
    return 9.1094*1e-31

print('''
Hello! It's a program that allows you to define the character of the flow of a liquid mixture through a pipeline.

Author: Aleksandra Gierczak

Enter data for calculations:

''')

t = float(input('Enter the temperature of the mixture t [C deg.]: '))
V = float(input('Enter the volumetric flow rate V [l/h]: '))
d = float(input('Enter the diameter of the pipeline d [m]: '))

print('''
Entering data for liquid no. 1:
''')

name1 = input('Enter the total formula of liquid no. 1: ')
cx1 = float(input('Enter the concentration of liquid no. 1 - cx1 [% mass]: '))
m1 = float(input('Enter the molar mass of liquid no. 1 - M1 [g]: '))
ro1 = float(input('Enter the density of liquid no. 1 - ρ1 [kg/m3]: '))
eta1 = float(input('Enter the viscosity of liwuid no. 1 - η1 [P*s]: '))

print('''
Entering data for liquid no. 2:
''')

name2 = input('Enter the total formula of liquid no. 2: ')
cx2 = float(input('Enter the concentration of liquid no. 2- cx2 [% mass]: '))
m2 = float(input('Enter the molar mass of liquid no. 2 - M2 [g]: '))
ro2 = float(input('Enter the density of liquid no. 2 - ρ2 [kg/m3]: '))
eta2 = float(input('Enter the viscosity of liwuid no. 2 - η2 [P*s]: '))

def moleFraction1(cxa, cxb, ma, mb):
    x1 = (cxa/ma)/((cxa/ma)+(cxb/mb))
    return x1
def moleFraction2(xa):
    x2 = 1 - x1
    return x2

x1 = moleFraction1(cx1, cx2, m1, m2)
x2 = moleFraction2(x1)

print(f'''
Mole fraction of liquid no. 1 - x1: {x1:.3f}''')
print(f'''
Mole fraction of liquid no. 2 - x2: {x2:.3f}
''')

def density(roa, rob, cxa, cxb):
    rom = (((cxa/100)/roa)+((cxb/100)/rob))**(-1)
    return rom

rom = int(density(ro1, ro2, cx1, cx2))

print(f'''Density of the mixture - ρm [kg/m3]: {rom}
''')

def viscosity(etaa, etab, xa, xb):
    etam = (etaa)**(xa) + (etab)**(xb)
    return etam

etam = viscosity(eta1, eta2, x1, x2)

print(f'''Viscosity of the mixture - [P*s]: {etam:.2e}
''')

from math import pi

def Reynolds(v, ro, sr, eta):
    re = (4*(v*(0.001/3600))*ro)/(pi*sr*eta)
    return re

re = int(Reynolds(V, rom, d, etam))

print(f'''Reynolds number: {re}''')

if re < 2320:
    print('Flow is laminar.')
elif re > 10000:
    print('Flow is turbulent.')
else:
    print('Flow is partially turbulent.')

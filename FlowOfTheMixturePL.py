print('''
Witaj w programie pozwalającym na określenie charakteru przepływu mieszaniny cieczy przez rurociąg.

Autor: Aleksandra Gierczak

Wprowadź dane do obliczeń:

''')

t = float(input('Wprowadź temperaturę mieszaniny t [st. C]: '))
V = float(input('Wprowadź objętościowe natężenie przepływu mieszaniny V [l/h]: '))
d = float(input('Wprowadź średnicę rurociągu d [m]: '))

print('''
Wprowadzanie danych dla cieczy pierwszej:
''')

name1 = input('Wprowadź wzór sumaryczny pierwszej cieczy: ')
cx1 = float(input('Wprowadź stężenie pierwszej cieczy cx1 [% wag]: '))
m1 = float(input('Wprowadź masę molową pierwszej cieczy M1 [g]: '))
ro1 = float(input('Wprowadź gęstość pierwszej cieczy ρ1 [kg/m3]: '))
eta1 = float(input('Wprowadź lepkość pierwszej cieczy η1 [P*s]: '))

print('''
Wprowadzanie danych dla cieczy drugiej:
''')

name2 = input('Wprowadź wzór sumaryczny drugiej cieczy: ')
cx2 = float(input('Wprowadź stężenie drugiej cieczy cx2 [% wag]: '))
m2 = float(input('Wprowadź masę molową drugiej cieczy M2 [g]: '))
ro2 = float(input('Wprowadź gęstość drugiej cieczy ρ2 [kg/m3]: '))
eta2 = float(input('Wprowadź lepkość drugiej cieczy η2 [P*s]: '))

def moleFraction1(cxa, cxb, ma, mb):
    x1 = (cxa/ma)/((cxa/ma)+(cxb/mb))
    return x1
def moleFraction2(xa):
    x2 = 1 - x1
    return x2

x1 = moleFraction1(cx1, cx2, m1, m2)
x2 = moleFraction2(x1)

print(f'''
Ułamek molowy pierwszej cieczy x1: {x1:.3f}''')
print(f'''
Ułamek molowy drugiej cieczy x2: {x2:.3f}
''')

def density(roa, rob, cxa, cxb):
    rom = (((cxa/100)/roa)+((cxb/100)/rob))**(-1)
    return rom

rom = int(density(ro1, ro2, cx1, cx2))

print(f'''Gęstość mieszaniny ρm [kg/m3]: {rom}
''')

def viscosity(etaa, etab, xa, xb):
    etam = (etaa)**(xa) + (etab)**(xb)
    return etam

etam = viscosity(eta1, eta2, x1, x2)

print(f'''Lepkość mieszaniny ηm [P*s]: {etam:.2e}
''')

from math import pi

def Reynolds(v, ro, sr, eta):
    re = (4*(v*(0.001/3600))*ro)/(pi*sr*eta)
    return re

re = int(Reynolds(V, rom, d, etam))

print(f'''Liczba Reynoldsa: {re}''')

if re < 2320:
    print('Przepływ jest laminarny.')
elif re > 10000:
    print('Przepływ jest burzliwy.')
else:
    print('Przepływ jest częściowo burzliwy.')

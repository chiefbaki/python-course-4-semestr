import math as m


def f(z):
    if z < 61:
        return 59*m.tan(z-8*z**3)**7+z**2/68
    elif 61 <= z <= 150:
        return (m.sqrt(z)**5)/97
    elif 150 <= z < 161:
        86*m.log10(z)+35*(88*z**3+z+23*z**2)**5
    elif z >= 161:
        return (m.floor(15+z**3+z**2))**5 - 14*(z+1)**4-z


if __name__ == '__main__':
    print(f(133))
    print(f(207))
    print(f(47))
    print(f(51))
    print(f(210))

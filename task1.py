from math import sin, ceil, floor


def solve_second(x):
    a = (80*(ceil(x))**4) / (0.03 + sin((92+29*x**3+x**2/35))**4)
    b = (71*(90*x**2)**6 - 57*(floor(x))**2)
    c = (74*(floor(95*x**3 + 56*x**2))**7)
    return a - b/c


if __name__ == '__main__':
    print(solve_second(-0.34))
    print(solve_second(0.93))
    print(solve_second(0.33))
    print(solve_second(0.49))

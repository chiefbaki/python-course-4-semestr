import math as m


def main(*lst):
    def fun(a, b, c):
        return (9 * a ** 2 - b ** 3 - c / 87) ** 7

    y, x, z = lst
    res = 0
    for i in range(1, len(x) + 1):
        res += fun(x[len(x)-i], y[len(y)-m.ceil(i/2)],
                   z[len(z)-m.ceil(i/4)])
    return res * 48



if __name__ == '__main__':
    print(main([-0.68, 0.16], [-0.57, -0.74], [0.84, 0.24]))  # 3.44e+06
    print(main([-0.71, -0.28], [0.15, 0.17], [-0.49, 0.24]))  # 7.63e-03
    print(main([0.69, 0.99], [-0.28, 0.59], [-0.94, -0.48]))  # 1.08e+04
    print(main([0.45, 0.65], [0.94, -0.16], [0.54, 0.55]))  # 7.51e+07
    print(main([0.1, 0.31], [0.73, 0.54], [0.13, 0.04]))  # 2.72e+06

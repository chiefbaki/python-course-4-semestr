import math as m


def main(m, a, p):
    cnt = 0
    for i in range(1, a+1):
        for c in range(1, m+1):
            cnt += (61*(6 + c**2/97 + 55*p)**2 + i**5 + 77*p**6)
    return cnt


if __name__ == '__main__':
    print(main(5, 7, -0.41))
    print(main(4, 5, -0.18))
    print(main(3, 8, -0.62))
    print(main(8, 5, 0.28))
    print(main(5, 5, -0.05))

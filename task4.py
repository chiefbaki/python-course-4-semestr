def main(n):
    if n == 0:
        return -0.19
    elif n >= 1:
        return 94 * (93 + main(n - 1) / 30) + main(n-1) + 11


print(main(7))
print(main(2))
print(main(8))
print(main(3))
print(main(6))

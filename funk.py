import sys
import math


def read_coef(name, idx):
    if idx < len(sys.argv):
        try:
            return float(sys.argv[idx])
        except:
            print("Плохой коэффициент", name, "в argv, введите заново")
    while True:
        try:
            return float(input("Введите " + name + ": "))
        except:
            print("Ошибка, нужно число")


def from_t(t):
    if t > 0:
        x = math.sqrt(t)
        return [-x, x]
    if t == 0:
        return [0.0]
    return []


def solve(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return "inf"
    if a == 0 and b == 0:
        return []
    if a == 0:
        return from_t(-c / b)

    D = b * b - 4 * a * c

    if D < 0:
        return []
    if D == 0:
        return from_t(-b / (2 * a))

    sq = math.sqrt(D)
    t1 = (-b - sq) / (2 * a)
    t2 = (-b + sq) / (2 * a)
    all_roots = from_t(t1) + from_t(t2)

    unique = []
    for r in all_roots:
        if r not in unique:
            unique.append(r)
    unique.sort()
    return unique


def main():
    a = read_coef("A", 1)
    b = read_coef("B", 2)
    c = read_coef("C", 3)
    print(a, "*x^4 +", b, "*x^2 +", c, "= 0")
    if a == 0:
        print("A = 0, не биквадратное")
    res = solve(a, b, c)
    if res == "inf":
        print("Бесконечно много корней")
    elif res == []:
        print("Корней нет")
    else:
        print("Корни:", res)


if __name__ == "__main__":
    main()
import sys
import math


def to_float(s):
    try:
        return float(s)
    except:
        return None


def get_coef(name, idx):
    if idx < len(sys.argv):
        v = to_float(sys.argv[idx])
        if v is not None:
            return v
        print("Плохой коэффициент", name, "в argv, введите заново")
    while True:
        v = to_float(input("Введите " + name + ": "))
        if v is not None:
            return v
        print("Ошибка, нужно число")


def solve(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "inf"
            return []
        t = -c / b
        if t < 0:
            return []
        if t == 0:
            return [0.0]
        x = math.sqrt(t)
        return [-x, x]

    D = b * b - 4 * a * c
    if D < 0:
        return []

    if D == 0:
        t = -b / (2 * a)
        if t < 0:
            return []
        if t == 0:
            return [0.0]
        x = math.sqrt(t)
        return [-x, x]

    sq = math.sqrt(D)
    t1 = (-b - sq) / (2 * a)
    t2 = (-b + sq) / (2 * a)
    roots = []
    for t in (t1, t2):
        if t > 0:
            x = math.sqrt(t)
            if -x not in roots:
                roots.append(-x)
            if x not in roots:
                roots.append(x)
        elif t == 0:
            if 0.0 not in roots:
                roots.append(0.0)
    roots.sort()
    return roots


def main():
    a = get_coef("A", 1)
    b = get_coef("B", 2)
    c = get_coef("C", 3)
    print(a, "*x^4 +", b, "*x^2 +", c, "= 0")
    if a == 0:
        print("A = 0, не биквадратное")
    res = solve(a, b, c)
    if res == "inf":
        print("Бесконечно много корней")
    elif not res:
        print("Корней нет")
    else:
        print("Корни:", res)


if __name__ == "__main__":
    main()
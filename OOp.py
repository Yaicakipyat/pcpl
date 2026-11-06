import sys
import math


class Reader:
    def __init__(self, argv):
        self.argv = argv

    def read(self, name, idx):
        if idx < len(self.argv):
            try:
                return float(self.argv[idx])
            except:
                print("Плохой коэффициент", name, "в argv, введите заново")
        while True:
            try:
                return float(input("Введите " + name + ": "))
            except:
                print("Ошибка, нужно число")


class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        a, b, c = self.a, self.b, self.c

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
            elif t == 0 and 0.0 not in roots:
                roots.append(0.0)
        roots.sort()
        return roots


class App:
    def __init__(self, argv):
        self.reader = Reader(argv)

    def run(self):
        a = self.reader.read("A", 1)
        b = self.reader.read("B", 2)
        c = self.reader.read("C", 3)
        print(a, "*x^4 +", b, "*x^2 +", c, "= 0")
        if a == 0:
            print("A = 0, не биквадратное")
        res = Equation(a, b, c).solve()
        if res == "inf":
            print("Бесконечно много корней")
        elif not res:
            print("Корней нет")
        else:
            print("Корни:", res)


if __name__ == "__main__":
    App(sys.argv).run()
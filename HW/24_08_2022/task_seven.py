def calc(one: int, two: int, three: int, four: int, five: int) -> int:
    list_calc = [one, two, three, four, five]
    list_calc.sort()

    return list_calc[0]


class Calc:

    def __init__(self):
        self.int_five_int = input("Введите числа(5 штук):")
        self.list_five_int = self.int_five_int.split()
        self.one = int(self.list_five_int[0])
        self.two = int(self.list_five_int[1])
        self.three = int(self.list_five_int[2])
        self.four = int(self.list_five_int[3])
        self.five = int(self.list_five_int[4])

    def go(self):
        return calc(self.one, self.two, self.three, self.four, self.five)


calc1 = Calc()
print("Минимальное число из введеных: ", calc1.go())

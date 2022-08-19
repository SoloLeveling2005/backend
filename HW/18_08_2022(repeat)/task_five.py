

def calc():
    try:
        first = int(input("Введите первое число:"))
        second = int(input("Введите второе число:"))

        while True:
            if first == second:
                break
            if int(first)%7 == 0:
                print(first)
            first += 1

    except ValueError:
        print("Это не числа")
        calc()
calc()
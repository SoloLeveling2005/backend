

def check():
    global ints
    int_one = input("Введите числа через пробел:")
    int_one = int_one.split(" ")
    int_one = [x for x in int_one if x]
    ints = []
    for i in int_one:
        ints.append(int(i))
    try:
        correct = 0
        if int(ints[0]) == int(ints[1]):
            print("Они равны")
            correct = 1
        elif ints[0] != ints[1]:
            ints.sort()
            print("Они не равны")
            print(ints)
            correct = 1
    except ValueError:
        print("Это не числа")
    finally:
        if correct == 0:
            print("Вы ввели не число")
            check()


check()


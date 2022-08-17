import traceback


def ints():
    one_int = input("Введите первое число:")
    two_int = input("Введите второе число:")
    three_int = input("Введите третье число:")

    try:
        summ = int(one_int) + int(two_int) + int(three_int)
        print("Сумма чисел = ", summ)
        mult = int(one_int) * int(two_int) * int(three_int)
        print("Произведение чисел = ", mult)
    except ValueError:
        print("Вы ввели не целые числа, повторите ввод.")
        ints()

ints()
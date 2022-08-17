import traceback


def calc():
    one_int = input("Введите первое число:")
    two_int = input("Введите второе число:")
    three_int = input("Введите третье число:")

    try:
        summ = str(one_int) + str(two_int) + str(three_int)
        print("Ваше число = ", summ)

    except ValueError:
        print("Вы ввели не целые числа, повторите ввод.")
        calc()


calc()

import traceback


def calc():
    one_int = input("Введите число:")


    try:
        exit_int = 1
        for i in str(one_int):
            exit_int *= int(i)

        print("Ваше число = ", exit_int)

    except ValueError:
        print("Вы ввели не число, повторите ввод.")
        calc()


calc()

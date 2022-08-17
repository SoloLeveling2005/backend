import traceback


def calc():
    one_int = input("Введите количество метров:")


    try:
        print("метры = ", int(one_int)*1)
        print("дециметры = ", int(one_int)*10)
        print("сантиметры = ", int(one_int)*100)
        print("милиметры = ", int(one_int)*1000)

    except ValueError:
        print("Вы ввели не число, повторите ввод.")
        calc()


calc()
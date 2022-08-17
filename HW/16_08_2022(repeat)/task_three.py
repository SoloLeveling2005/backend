import traceback

def calc():
    print("Площадь ромба: S=ah")
    one_int = input("Введите длину основания:")
    two_int = input("Введите высоту:")


    try:
        calc_S = int(one_int) * int(two_int)
        print("Площадь ромба = ", calc_S)
    except:
        try:
            calc_S = float(one_int) * float(two_int)
            print("Площадь ромба = ", calc_S)
        except ValueError:
            print("Вы ввели не числа, повторите ввод.")
            calc()

calc()
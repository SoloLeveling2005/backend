

def calc():
    list_range = []
    try:
        first = int(input("Введите первое число:"))
        second = int(input("Введите второе число:"))

        while True:
            list_range.append(first)
            if first == second:
                break


            first += 1
        all_element = ""
        for i in list_range:
            all_element += (str(i) + " ")
        print("Все числа диапазона:", all_element)
        # 2
        all_element = ""
        list_range.sort(reverse=True)
        for i in list_range:
            all_element += (str(i) + " ")
        print("Все числа диапазона в убывающем порядке:", all_element)
        # 3
        str_division_seven = ""
        for i in list_range:
            if i%7 == 0:
                str_division_seven += (str(i) + " ")
        print("Число кратное 7:", str_division_seven)
        # 4
        int_division_five = 0
        for i in list_range:
            if i%5 == 0:
                int_division_five += 1
        print("Чисел кратных 5:", int_division_five,"штук")
    except ValueError:
        print("Это не числа")
        calc()

calc()
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

        for i in list_range:
            if i%3==0 and i%5==0:
                print("Fizz Buzz")
            elif i%3==0:
                print("Fizz")
            elif i%5==0:
                print("Buzz")
            if i%3!=0 and i%5!=0:
                print(i)


    except ValueError:
        print("Это не числа")
        calc()

calc()
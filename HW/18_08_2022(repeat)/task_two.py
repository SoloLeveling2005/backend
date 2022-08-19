
days = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
def check():
    day = input("Введите число:")
    global correct
    try:
        correct = 0
        for i in days:
            index = days.index(i)
            if int(day) == (index+1):
                print(i)
                correct = 1
                break
    finally:
        if correct == 0:
            print("Вы ввели неправильное число")
            check()


check()

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
def check():
    day = input("Введите число(0-6):")
    global correct
    try:
        correct = 0
        for i in days:
            index = days.index(i)
            if int(day) == (index):
                print(i)
                correct = 1
                break
    finally:
        if correct == 0:
            print("Вы ввели неправильное число")
            check()


check()





# import datetime
# import calendar
#
# year = datetime.date.today().year
# month = datetime.date.today().month
#
# day = input("Введите число:")
#
# norbert_birthday = datetime.date(year=year, month=month, day=int(day))
# print(norbert_birthday)
# print(calendar.day_name[norbert_birthday.weekday()])
# dayy = calendar.day_name[norbert_birthday.weekday()]
# days = [["Monday", "Понедельник"], ["Tuesday", "Вторник"], ["Wednesday", "Среда"], ["Thursday", "Четверг"],
#         ["Friday", "Пятница"], ["Saturday", "Суббота"], ["Sunday", "Воскресенье"]]
# for i in days:
#     if i[0] == dayy:
#         print(i[1])
#


#
# def check():
#     day = input("Введите число:")
#     global correct
#     try:
#         correct = 0
#         dateTime = datetime.datetime(2021, 1, int(day), 00, 00, 00)
#         print(dateTime.weekday())
#     finally:
#         if correct == 0:
#             print("Вы ввели неправильное число")
#             check()
#
#
# check()
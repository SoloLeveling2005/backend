import traceback


def pay():
    salary = input("Зарплата за месяц:")
    credit = input("Сумма месячного платежа по кредиту в банке:")
    utilities = input("Задолженность за коммунальные услуги:")

    try:
        money = float(salary) - float(credit) - float(utilities)
        if money < 0:
            print("Вы должны ", (money * (-1)))
        elif money >= 0:
            print("У вас осталось ", money)
    except ValueError:
        print("Вы ввели не числа, повторите ввод.")
        pay()


pay()

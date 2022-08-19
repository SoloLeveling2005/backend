"Number is positive»,"
"если меньше нуля «Number is negative», если равно нулю"
"«Number is equal to zero»"



def calc():
    intt = input("Введите число:")
    try:
        if float(intt) < 0:
            print("Number is negative")
        elif float(intt) > 0:
            print("Number is positive")
        elif float(intt) == 0:
            print("Number is equal to zero")
    except ValueError:
        print("Это не число")
        calc()
calc()
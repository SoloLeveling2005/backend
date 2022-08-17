import time
import traceback


def calc():
    global list_text, new_list_text
    text = input("Введите:")
    list_text = []
    # list_text = str(text).split("")

    for char in text:
        list_text.append(char)

    len_list = len(list_text)
    print(len_list)
    new_list_text = ""
    var = len(list_text)
    while True:
        if var != 0:
            var -= 1
            index = list_text[var]
            new_list_text += str(index)
        else:
            print("Ваше число = ", new_list_text)
            break




calc()

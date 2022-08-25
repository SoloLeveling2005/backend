user_range = input("Введите два числа(диапазон, например: 2 20): ")
list_user_range = user_range.split(" ")
list_user_range.sort(reverse=True)
user_range = {
    "top": list_user_range[0],  # Верх диапазона
    "bottom": list_user_range[1],  # Низ диапазона
}
print(user_range["top"])


def mult(input_range):
    list_vars = []
    for i in range(int(input_range["bottom"]), int(input_range["top"]) + 1):
        list_vars.append(i)
    print(list_vars)
    result = 1
    for i in list_vars:
        result = result * i

    return result


print(mult(user_range))

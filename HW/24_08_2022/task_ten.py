str_int = input("Введите число: ")


list_one = [i for i in str_int]
print(list_one)



list_two = [ii for ii in str_int][::-1]

print(list_two)

if list_one == list_two:
    print("Это палиндром")
elif list_one != list_two:
    print("Это не палиндром")
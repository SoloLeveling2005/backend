import re


var = input("Введите длину стороны квадрата, символ и переменную логического типа")

print(re.search("([0-9])", var).group())
print("Периметр: ", int((re.findall(r'[0-9]+', var))[0])*4)
print("Площадь: ", int((re.findall(r'[0-9]+', var))[0])**2)
print("Символ(ы): ", (re.findall(r'[a-zA-Z]+', var))[0])
if re.findall("False\Z", var):
    print("Квадрат пустой")
elif re.findall("True\Z", var):
    print("Квадрат полный")

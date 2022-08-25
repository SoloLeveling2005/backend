import re
by1 = input("От: ")
to1 = input("До: ")
# def get_param(by=3,to=10):
#     # Не получилось как сверху поэтому пришлось добавлять два условия
#
#     for i in range(by,to+1):
#         if i != 0:
#             if re.search(r'[24680]', str(i)):
#                 print(i)
#
# get_param(int(by1),int(to1))

# или

print("Четные числа в диапазоне от ",by1," до ",to1)
[print(i) for i in range(int(by1),int(to1)+1) if i % 2 == 0]

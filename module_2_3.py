my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
print('Положительные числа по порядку из списка: ')
while a < len(my_list):
    if my_list[a] > 0:
        print(my_list[a])
        a += 1
        continue
    elif my_list[a] == 0:
        a += 1
    else:
        print('Встретилось отрицательное число ', my_list[a])
        break
print('Список закончился')
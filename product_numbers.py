# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
import math
list_in = []
N = int(input('Введите количество чисел в списке: '))
for i in range(N):
        temp = int(input('Введите число: '))
        list_in.append(temp)
print('Введённый список: ')
print(list_in)
list_out = []
for i in range(math.ceil(N/2)):
    list_out.append(list_in[i] * list_in[len(list_in) - i - 1])
print(list_out)
# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

list = []
N = int(input('Введите количество чисел в списке: '))
for i in range(N):
        temp = int(input('Введите число: '))
        list.append(temp)
print('Введённый список: ')
print(list)
summ = 0
for i in range(0, N, 2):
    summ += list[i]
print('Сумма элементов, стоящих на нечётных позициях = ', summ)
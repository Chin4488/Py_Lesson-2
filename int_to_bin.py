# Написать программу преобразования десятичного числа в двоичное.

number = int(input('Введите десятичное число: '))
bit = ''
while number > 0:
    bit = str(number % 2) + bit
    number = number // 2
print('Двоичное число:', bit)
# Написать программу преобразования двоичного числа в десятичное.

number = input("Введите двоичное число: ")
temp = 0
for i in range(len(number)):
    temp += int(number[i]) * (2**(len(number) - i - 1))
print('Десятичное число: ' + str(temp))

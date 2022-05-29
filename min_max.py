# В заданном списке вещественных чисел найдите разницу между 
# максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def remains(n):
    decimal = divmod(n, 1)
    return round(list(decimal)[1], 10)

list_in = [1.1, 1.2, 3.1, 5, 10.01]
list_part = []
for i in range(len(list_in)):
    if remains(list_in[i]) != 0:
        list_part.append(remains(list_in[i]))
print(list_in, "=>", (max(list_part) - min(list_part)))

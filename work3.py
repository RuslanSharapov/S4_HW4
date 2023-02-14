#   Задайте последовательность чисел. Напишите программу, 
#   которая выведет список неповторяющихся элементов исходной последовательности.

import random

n = int(input('Введите число: '))
my_list = []
new_list = []
for i in range(n):
    my_list.append(random.randint(1, 9))
print(my_list)
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

# С применением встроенной функции set

""" import random

n = int(input('Введите число: '))
my_list = []

for i in range(n):
    my_list.append(random.randint(1, 9))
print(my_list)
print(list(set(my_list))) """


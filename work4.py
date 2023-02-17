#    Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
#   (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

#   Пример:
#   - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень k: '))

coefficients = [random.randint(0, 100) for i in range(k + 1)]
polynom = '+'.join([f'{a}x*{i}' for i, a in enumerate(coefficients) if a][::-1])
print(polynom)
polynom = polynom.replace('x*1+', 'x+')
polynom = polynom.replace('x*0', '')
with open('my_text.txt', 'w') as data:
    data.write(polynom)

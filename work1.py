# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint
degree = int (input ('Введите натуральную степень k: '))
number_1 = randint(0, 100)
number_2 = randint(0, 100)
print(f'{number_1}*x^{degree} + {number_2}*x + 5 = 0')
with open('task_4_1.txt', 'w') as data:
    data.write(f'{number_1}*x^{degree} + {number_2}*x + 5 = 0')
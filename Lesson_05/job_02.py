# Написать функцию, принимающую сколько угодно параметров (в том числе и 0) и возвращающую их сумму.

from decimal import Decimal


def sum_numbers(num):
    sum = 0
    for i in num:
        try:
            sum += Decimal(i)
        except:
            error.append(i)
    print('')
    print('Данные параметры с числами не удалось суммировать:', *error, sep='\n')
    print('')
    return print('Сумма всех чисел =', sum)


value = []
error = []

print('Найдем сумму всех вводимых параметров. Как только ввод будет завершен, напишите: стоп')
print('')
while True:
    x = input('Вводим параметр:')
    if x == 'стоп':
        break
    else:
        value.append(x)

sum_numbers(value)

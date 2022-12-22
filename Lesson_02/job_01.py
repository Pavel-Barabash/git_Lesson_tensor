'''
Задание 1: Пользователь вводит два числа (возможно дробные), вывести результат их:
    сложения, вычитания, умножения, деления,
    возведения в степень, деления по модулю,
    целочисленного деления.
'''


from decimal import Decimal


def start(dig):
    """Если ввели число, возращаем значение, иначе повторный ввод"""
    if dig.replace('.', '').isdigit() == True:
        num = Decimal(dig)
        return (num)
    else:
        print(dig, 'не является числом')
        print('')
        return (start(input('Введите повторно число: ')))


a = start(input('Введите первое число: '))
print('')
b = start(input('Введите второе число: '))


print('')
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
print(a, '/', b, '=', a / b)
print(a, '**', b, '=', a**b)
print(a, '%', b, '=', a % b)
print(a, '//', b, '=', a // b)

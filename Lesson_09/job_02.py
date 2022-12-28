'''
Задание 1: Пользователь вводит два числа (возможно дробные), вывести результат их:
    сложения, вычитания, умножения, деления,
    возведения в степень, деления по модулю,
    целочисленного деления.
'''


from decimal import Decimal


def sum_dig(num1, num2):
    """сложение 2ух чисел"""
    return num1 + num2


def dif_dig(num1, num2):
    """разность 2ух чисел"""
    return num1 - num2


def multi_dig(num1, num2):
    """умножение 2ух чисел"""
    return num1 * num2


def divis_dig(num1, num2):
    """деление 2ух чисел"""
    return num1 / num2


def expo_dig(num1, num2):
    """возведение в степень 2ух чисел"""
    return num1 ** num2


def div_modul_dig(num1, num2):
    """деление по модулю 2ух чисел"""
    return num1 % num2


def int_div_dig(num1, num2):
    """целочисленные деления 2ух чисел"""
    return num1 // num2


a = Decimal(input('Введите первое число: '))
print('')
b = Decimal(input('Введите второе число: '))


print('')
print(a, '+', b, '=', sum_dig(a, b))
print(a, '-', b, '=', dif_dig(a, b))
print(a, '*', b, '=', multi_dig(a, b))
print(a, '/', b, '=', divis_dig(a, b))
print(a, '**', b, '=', expo_dig(a, b))
print(a, '%', b, '=', div_modul_dig(a, b))
print(a, '//', b, '=', int_div_dig(a, b))

'''
Задание 4: C обработкой отрицательного дискриминанта (с комплексными числами),
            со случаем, если коэффициенты являются комплексными числами.
'''

print('Давайте решим квадратное уравнение, которое имеет вид:')
print('')
print('ax**2 + bx + c = 0')
print('')
type_num = input('Коэффициенты уравнения будут комплексными?(да\нет): ')
print()
print('Введите коэффициенты уравнения:')

if type_num == 'да':
    """Блок при условии работы с комплексными числами"""
    print('пример ввода комплексного числа: 1+2j')
    while True:
        a = complex(input('a = '))
        if a != complex(0):
            break
        print('"a" может быть любым числом, кроме 0. Повторите ввод:')
    b = complex(input('b = '))
    c = complex(input('c = '))
    print('')

    discrim = b**2 - 4*a*c
    print('Дискриминант равен:', discrim)
    print('')

    if discrim == complex(0):
        x = -b / (2*a)
        print('Корень данного уровнения:')
        print('x =', x)
    else:
        x1 = (-b + discrim**0.5) / (2*a)
        x2 = (-b - discrim**0.5) / (2*a)
        print('Корни данного уровнения:')
        print('x1 =', x1)
        print('x2 =', x2)


else:
    """Блок по работе с целыми числами"""
    while True:
        """Проверяем переменную 'a', не должна равняться нулю"""
        a = float(input('a = '))
        if a != 0:
            break
        print('"a" может быть любым числом, кроме 0. Повторите ввод:')
    b = float(input('b = '))
    c = float(input('c = '))
    print('')

    discrim = b**2 - 4*a*c

    print('Дискриминант равен:', discrim)

    if discrim > 0:
        x1 = (-b + discrim**0.5) / (2*a)
        x2 = (-b - discrim**0.5) / (2*a)
        print('Корни данного уровнения:')
        print('x1 =', x1)
        print('x2 =', x2)
    elif discrim == 0:
        x = -b / (2*a)
        print('Корень данного уровнения:')
        print('x =', x)
    else:
        x1 = complex(-b, ((discrim*-1)**0.5)) / (2*a)
        x2 = complex(-b, -((discrim*-1)**0.5)) / (2*a)
        print('Корни данного уровнения:')
        print('x1 =', x1)
        print('x2 =', x2)

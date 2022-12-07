# Задание 3: Написать скрипт решения квадратного уравнения
# модуль math не подключал для выведения корня

print('Давайте решим квадратное уравнение, которое имеет вид:')
print('')
print('ax**2 + bx + c = 0')
print('')
print('Введите коэффициенты уравнения:')

while True:
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
    print('Корней нет')

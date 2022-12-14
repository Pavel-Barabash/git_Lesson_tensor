'''
Написать функцию, принимающую строку-пароль.
Функция должна проверить подходит ли этот пароль условиям
и вернуть True - если подходит; False - если не подходит. Условия:   
    Должен быть не менее 6 символов;
    Должен содержать хотя бы одну цифру;
    Не должен состоять только из цифр;
    Не должен содержать слово “password” в любом регистре.
'''


def password(pas):
    f1 = f2 = f3 = False
    for i in list(pas):
        if i.isdigit():
            f1 = True
        elif not i.isdigit():
            f2 = True
    if 'password' not in pas.lower():
        f3 = True
    if len(pas) >= 6 and f1 and f2 and f3:
        return True
    else:
        return False


print('Условия пароля:')
print('Должен быть не менее 6 символов;')
print('Должен содержать хотя бы одну цифру')
print('Не должен состоять только из цифр;')
print('Не должен содержать слово “password” в любом регистре.')
print('')
in_pass = password(input('Введите пароль: '))

if in_pass:
    print('Надежный пароль')
else:
    print('Пароль не удовлетворяет требованиям')

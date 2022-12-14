# Написать функцию, которая возвращает заданное число Фибоначчи. Обязательно через рекурсию.

def fib(num):

    if num >= 0:
        if num == 0:
            return 0
        elif num == 1 or num == 2:
            return 1
        return fib(num - 1) + fib(num - 2)
    else:
        if num == -1:
            return 1
        elif num == -2:
            return -1
        return fib(num + 2) - fib(num + 1)


try:
    print(fib(int(input('Значение какого числа Фибоначчи Вас интересует: '))))
except:
    print('Необходимо было ввести целое число')

'''
Написать функцию. Для неё написать декораторы для следующего функционала:
    логирование выполнения функции;
    время выполнения функции;
    замедлить выполнение кода. Ограничить частоту вызова функции.
'''

import logging
import time


def dec_log(func):
    '''Декоратор логирования функции'''
    def wrapper():
        logging.basicConfig(level='DEBUG', filename='mylog.log')
        print('Лог отправлен в файл mylog.log')
        print('Start')
        func()
        logging.debug("Hello World, i'm debug")
        logging.info("Hello World, i'm info")
        logging.warning("Hello World, i'm warning")
        logging.error("Hello World, i'm error")
        logging.critical("Hello World, i'm critical")
        print('End')
    return wrapper


def dec_time(func):
    '''Время выполнения функции'''
    def wrapper():
        print('Start')
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print(f'Время выполнения функции {end_time-start_time:0.6f}')
        print('End')
    return wrapper


def dec_sleep(func):
    '''Замедляем частоту использования функции'''
    def wrapper():
        print('Start')
        start_time = time.perf_counter()
        time.sleep(5)
        func()
        end_time = time.perf_counter()
        print(f'Время выполнения функции, после ее замедления:')
        print(f'{end_time - start_time:0.0f} секунд')
        print('End')
    return wrapper


def draw_triangle():
    """Выводим автоматически лесенку из звездочек от 1 до 10 штук"""
    for i in range(1, 11):
        print('*' * i)
    return "😎"


print('Выведем лесенку, с которой будем работать')
draw_triangle()

print('')
print('Продемонстрируем 3 действия, с помощью декораторов:')
print('1) логирование выполнения функции')
print('2) время выполнения функции')
print('3) замедляем выполнение кода. Ограничиваем частоту вызова функции.')
request = int(input('Введите действие(1,2,3): '))

if request == 1:
    dec_twin = dec_log(draw_triangle)
    dec_twin()
elif request == 2:
    dec_twin = dec_time(draw_triangle)
    dec_twin()
elif request == 3:
    dec_twin = dec_sleep(draw_triangle)
    dec_twin()
else:
    print('Команда введена не верно')

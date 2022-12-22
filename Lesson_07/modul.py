"""Модуль содержит функции: массив дата/время и лесенка."""

from datetime import datetime

import numpy as np


def my_date_mas():
    """Выводим текущее время и дату, создаем матрицу, транспонируем ее."""
    print('Выводим текущее время и дату:')
    print(cur_dat)

    print('')
    print('Создадим матрицу по значениям даты\времени:')
    mas = np.array([[year, mouth, day], [hour, minute, sec]])
    print(mas)

    print('')
    print('Транспонируем матрицу:')
    return mas.transpose()


def draw_triangle():
    """Выводим автоматически лесенку из звездочек от 1 до 10 штук"""
    for i in range(1, 11):
        print('*' * i)
    return "😎"


# Переменные
cur_dat = datetime.now()
year = cur_dat.year
mouth = cur_dat.month
day = cur_dat.day
hour = cur_dat.hour
minute = cur_dat.minute
sec = cur_dat.second

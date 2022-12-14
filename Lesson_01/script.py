#!/usr/bin/python3
import random


# Создаем список ответов
answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
           "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
           "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
           "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
           "Перспективы не очень хорошие", "Весьма сомнительно"]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('')
name = input('Как тебя зовут? ')
print('')
print('Поиграем', name)


def start_game():
    """Запрашиваем вопрос и выдаем случайны ответ из списка: answers"""
    while True:
        print('Отвечу на любой твой вопрос! Задавай скорее, я жду:')
        print('')
        reply = input()
        option = random.choice(answers)
        print(option)
        break
    again_game()
    return


def stop_game():
    """Завершение программы"""
    print('Очень жаль, как только появятся вопросы, сразу возвращайся;)')
    return ()


def again_game():
    """запрос о повтоной игре, принимаем ответ на латинице\кириллице"""
    text = input('Сыграем еще раз?')
    print('')
    if text.lower() == 'да' or text.lower() == 'yes':
        start_game()
        return
    else:
        stop_game()


start_game()

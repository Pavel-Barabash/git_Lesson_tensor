'''
Создать игровой инвентарь.
Должна быть возможность добавлять/удалять предметы из него.
Инвентарь должен быть ограничен по весу, каждый предмет имеет свой вес.
Вывод предметов должен быть с названием предмета и его весом.
'''


def start():
    """Основное меню с действиями инвентаря.


    Добавить, удалить, проверить, завершить.


    """
    print('Доступные действия:')
    print('1) Добавить предмет')
    print('2) Удалить предмет')
    print('3) Проверить инвентарь')
    print('0) Завершить сборку инвентаря')
    actions = input('Введите цифру зароса: ')
    if actions == '1':
        app_items()
    elif actions == '2':
        del_items()
    elif actions == '3':
        check_items()
    elif actions == '0':
        stop()
    else:
        print('')
        print('Выбирите пожалуйста ответ из доступных вариантов, повторим...')
        start()


def app_items():
    """Позволяет добавлять предметы, вес, проверка по весу.


    item -- добавляемый предмет
    weight -- Вес предмета
    Проверяем есть в инвентаре новый предмет, если нет,
    добавляем в список inventory.
    Проверяем ограничение по весу, если в пределах нормы,
    добавляем вес в weight_item.


    """
    print('')
    item = input('Какой предмет Вы хотите добавить?: ')
    weight = int(input('Укажите его вес: '))
    weight_item.append(weight)
    if item in inventory:
        if input('Аналогичный предмент уже есть, снять его?(да\нет): ') == 'да':
            del_items()
        else:
            print('')
            start()
    elif sum(weight_item) > 40:
        print('к сожалению, с данным предметом мы превышаем общий вес в 40кг.')
        del weight_item[-1]
        check_items()
    else:
        inventory[item] = weight
        check_items()


def del_items():
    """Удаление предмета из инвентаря.


    item_del -- удаляемый предмет
    Проверяем какие предметы лежат в инвентаре,
    если пустой, запускаем функцию app_items.
    При удалении предмета, также вычитаем вес из weight_item.


    """
    print('')
    if not inventory:
        print('на данный момент инвентарь пустой')
        app_items()
    else:
        print('В инвентаре лежат предметы: ')
        for key in inventory:
            print(key)
        item_del = input('Какой элемент хотим удалить?: ')
        weight_item.append(inventory[item_del]*-1)
        del inventory[item_del]
        print('Удаляем', item_del)
        print('')
        check_items()


def check_items():
    """Проверяем весь инвентарь в рюкзаке."""
    print('')
    if not inventory:
        print('на данный момент инвентарь пустой')
        app_items()
    else:
        print('Выводим в стиле "предмет: вес"')
        print('')
        for key, value in inventory.items():
            print(f'{key}: {value} кг.')
        print('')
        print('максимальный вес инвентаря: 40 кг.')
        print('общий вес на данный момент:', sum(weight_item), 'кг.')
        print('Инвентарь может вместить еще:', 40 - sum(weight_item), 'кг.')
        print('')
        print('')
        start()


def stop():
    """Завершение работы с инвентарем."""
    print('')
    if not inventory:
        if input(
            'Ты уверен что пойдешь в опасное приключение в чем мать родила?(да\нет): '
        ) == 'да':
            print('Хорошо, мы будем молиться за тебя...')
        else:
            start()
    else:
        print('Выводим в стиле "предмет: вес"')
        print('')
        for key, value in inventory.items():
            print(f'{key}: {value} кг.')
    print('')
    print('Интересный инвентарь.')
    print('На этой доброй ноте, отправляемся в путь, до скорых встреч...')
    return


inventory = {}      # Предметы инвентаря
weight_item = []    # Вес инвентаря

print('Собираемся в путь, надо собрать самое нужное в свой инвентарь,')
print('который на данный момент пуст. Ограничение по весу 40кг. Удачи!')
print('')
start()

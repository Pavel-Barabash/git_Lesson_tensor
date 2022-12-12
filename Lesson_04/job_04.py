# Создать игровой инвентарь. Должна быть возможность добавлять в него предметы и удалять предметы из него. Инвентарь должен быть ограничен по весу, каждый предмет имеет свой вес. Вывод предметов должен быть с названием предмета и его весом.

def start():
    actions = input('Доступные действия:\n1) Добавить предмет\n2) Удалить предмет\n3) Проверить инвентарь\n0) Завершить сборку инвентаря\nВведите цифру зароса: ')
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
    print('')
    item = input('Какой предмет Вы хотите добавить?: ')
    x = int(input('Укажите его вес: '))
    weight_item.append(x)
    if item in inventory:
        if input('Аналогичный предмент уже есть, хотите снять его?(да\нет): ') == 'да':
            del_items()
        else:
            print('')
            start()
    elif sum(weight_item) > 40:
        print('к сожалению, с данным предметом мы превышаем общий вес в 40кг.')
        del weight_item[-1]
        check_items()
    else:
        inventory[item] = x
        check_items()


def del_items():
    print('')
    if not inventory:
        print('на данный момент инвентарь пустой')
        app_items()
    else:
        print('В инвентаре лежат предметы: ')
        for key in inventory:
            print(key)
        x = input('Какой элемент хотим удалить?: ')
        weight_item.append(inventory[x]*-1)
        del inventory[x]
        print('Удаляем', x)
        print('')
        check_items()


def check_items():
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
    print('')
    if not inventory:
        if input('Ты уверен что пойдешь в опасное приключение в чем мать родила?(да\нет): ') == 'да':
            print('Хорошо, мы будем молиться за тебя...')
        else:
            start()
    else:
        print('Выводим в стиле "предмет: вес"')
        print('')
        for key, value in inventory.items():
            print(f'{key}: {value} кг.')
    print('')
    print('Интересный инвентарь. На этой доброй ноте, отправляемся в путь, до скорых встреч...')
    return

inventory = {}
weight_item = []

print('Собираемся в путь, надо собрать и положить самое необходимое в свой инвентарь, который на данный момент пуст. Ограничение по весу 40кг. Удачи!')
print('')
start()


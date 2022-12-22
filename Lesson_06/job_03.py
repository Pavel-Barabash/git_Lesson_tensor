'''
XOR шифрование/расшифрование.
На входе файл с текстом и ключ шифрования (строка),
на выходе преобразованное (зашифрованное/расшифрованное) сообщение в файле.
'''

import random


def xor_crypt(text):
    """Шифрование текста в Юникод.
    

    crypt -- список в формате Юникод после битовой операции текста и ключа
    crypt_chr -- перевод числового списка crypt в символ Юникода


    """
    crypt = list()
    for i in range(len(text)):
        crypt.append((text[i] ^ key[i]))
    crypt_chr = [chr(x) for x in crypt]
    with open('./data_job03/xor_crypt.txt', 'w') as file:
        file.write(''.join(crypt_chr))


def xor_decrypt(text):
    """Расшифровка Юникод символов в обычный текст    


    decrypt -- список в формате Юникод после битовой операции текста и ключа
    decrypt_chr -- перевод числового списка decrypt в текст


    """
    decrypt = list()
    for i in range(len(text)):
        decrypt.append((text[i] ^ key[i]))
    decrypt_chr = [chr(x) for x in decrypt]
    with open('./data_job03/xor_decrypt.txt', 'w') as file:
        file.write(''.join(decrypt_chr))


def key_ascii(key):
    """Переводим в числовое значение Юникод пароль"""
    key_pass = [ord(x) for x in key]
    if len(data) == 0:
        print('отсутвует текст для шифрования')
        return

    # Недостающее колличество, заполняем рандомными числами
    elif len(data) > len(key):
        for i in range(len(data)-len(key_pass)):
            key_pass.append(random.randint(0, 255))

    # Если ключ длинее текста для шифрования, удалим лишнее элементы
    elif len(data) < len(key):
        del key_pass[-(len(key) - len(data)):]

    return key_pass


with open('./data_job03/text_for_xor.txt', 'r') as file:
    data = [ord(dig) for dig in file.read()]

print('Производим шифрования\расшифрования файла: "text_for_xor.txt"')
print('')
key = key_ascii(input('Введите произвольный ключ для шифрования: '))

# Производим шифрование в символы Юникода
crypt_txt = xor_crypt(data)

with open('./data_job03/xor_crypt.txt', 'r') as file:
    data_crypt = [ord(dig) for dig in file.read()]

# Производим дешифрование
decrypt_txt = xor_decrypt(data_crypt)

print('')
print('Итоговый результат шифрования\расшифрования в файлах:')
print('xor_crypt.txt')
print('xor_decrypt.txt')

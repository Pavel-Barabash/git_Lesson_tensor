# Написать функцию преобразующую список строк, в список байт кодов. Написать обратную функцию.

def b_encode(text):
    return text.encode('utf-8')


def b_decode(text):
    return text.decode('utf-8')


text_en = b_encode(
    input('Введите текст, который хотим преобразовать в байт коды: '))
text_de = b_decode(text_en)

print('')
print('После преобразования, получаем битовую строку:')
print(text_en)

print('')
print('Преобразовываем в обычную строку:')
print(text_de)

# Реализовать сортировку списка методом пузырька

from random import randint

len_list = int(input('Создадим случайный список от 1 до 74, выберите колличество чисел в нем?: '))
list_sort = [randint(1, 74) for i in range(len_list)]


print('Необходимо отсортировать список:')
print(list_sort)
print('')

for i in range(len_list - 1):
    flag = True
    for j in range(len_list - i - 1):
        if list_sort[j] > list_sort[j+1]:
            list_sort[j], list_sort[j+1] = list_sort[j+1], list_sort[j]
            flag = False
    if flag == True:
        break
print('Сортируем методом пузырька, получаем результат:')
print(list_sort)

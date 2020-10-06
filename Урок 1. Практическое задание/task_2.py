"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""


# 1 O(n^2) - квадратичная
def min_lst_1(lst):
    for i in range(len(lst)):
        lst[i]
        for j in range(len(lst)):
            if lst[j] < lst[i]:
                break
    return lst[j]


# O(n) - линейная
def min_lst_2(lst):
    a = min(lst)
    return a


range_list = ([i for i in range(10, 100)])
# for i in range(len(range_list)):
#     print(range_list[i])

print(min_lst_1(range_list))
print(min_lst_2(range_list))

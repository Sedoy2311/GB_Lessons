# # Задание №1
#
#
# a = 15 * 3
# b = 15 / 3
# c = 15 // 2
# d = 15 ** 2
# print(type(a), type(b), type(c), type(d))
#
#
# # Задание №2
# # Решение с помощью модуля Re
#
#
# import re
#
# def convert_list_in_str():
#     """Обособим каждое целое число кавычками, дополним нулём до двух целочисленных разрядов и выведем с строку"""
#
#     new_list = []
#     for i in my_list:
#         if i.isdigit():
#             new_list.extend(['"', f'{i.zfill(2)}', '"'])
#         elif i.startswith('+'):
#             new_list.extend(['"', f'{i.zfill(3)}', '"'])
#         else:
#             new_list.append(i)
#     str_out = ' '.join(new_list)
#     return str_out
#
# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# regex = '"\s+([^"]+)\s+"'
# result = re.sub(regex, '"'+r'\1'+'"', convert_list_in_str())
# print(result)
#
#
# # Задание №3
# # Сразу добавим кавычки к числовым элементам списка
#
#
# def convert_list_in_str():
#     """Обособим каждое целое число кавычками, дополним нулём до двух целочисленных разрядов и выведем с строку, не создавая нового списка"""
#
#     for n, i in enumerate(my_list, 0):
#         if i.isdigit():
#             my_list[n] = (f'"{i.zfill(2)}"')
#         elif i.startswith('+'):
#             my_list[n] = (f'"{i.zfill(3)}"')
#     return ' '.join(my_list)
#
# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# result = convert_list_in_str()
# print(result)
#
#
# # Задание №4
# # Решаем через создание нового списка
#
#
# def convert_name_extract():
#     """Форматируем имена и преобразовыем в список приветствий"""
#
#     name = []
#     for i in my_list:
#         name.extend(['Привет, '+i.split()[-1].title()+'!'])
#         i = ' '.join(my_list)
#     list_out = ' '.join(name)
#     return list_out
#
# my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# result = convert_name_extract()
# print(result)
#
#
# # Решаем без создания нового списка
#
#
# def convert_name_extract():
#     """Форматируем имена и преобразовыем в список приветствий"""
#
#     for n, i in enumerate(my_list, 0):
#         my_list[n] = 'Привет, ' + i.split()[-1].title() + '!'
#     return ' '.join(my_list)
#
# my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# result = convert_name_extract()
# print(result)
#
#
# # Задание №5
#
# from random import uniform
#
#
# def transfer_list_in_str(list_in: list) -> str:
#     """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
#         формирует из них единую строковую переменную разделяя значения запятой."""
#     price = []
#     for i in my_list:
#         r = int(i)
#         k = (i - int(i)) * 100
#         numb = f'{r} руб {k:02.0f} коп'
#         price.append(numb)
#     str_out = ', '.join(price)
#     return str_out
#
#
# my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
# result_1 = transfer_list_in_str(my_list)
# print(result_1)
#
#
# def sort_prices(list_in: list) -> list:
#     """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
#     my_list.sort()
#     return my_list
#
#
# print(id(my_list)) # зафиксируйте здесь информацию по исходному списку my_list
# result_2 = sort_prices(my_list)
# print(id(result_2)) # зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
# print(result_2)
#
#
# def sort_price_adv(list_in: list) -> list:
#     """Создаёт новый список и возвращает список с элементами по убыванию"""
#     sort_revers = sorted(my_list, reverse=True)
#     list_out = sort_revers
#     return list_out
#
#
# result_3 = sort_price_adv(my_list)
# print(result_3)
#
#
# def check_five_max_elements(list_in: list) -> list:
#     """Проверяет элементы входного списка вещественных чисел и возвращает
#         список из ПЯТИ максимальных значений"""
#     sort_revers_max = sorted(my_list, reverse=True)
#     list_out = sort_revers_max[:5]
#     return list_out
#
#
# result_4 = check_five_max_elements(my_list)
# print(result_4)
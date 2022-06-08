def get_numbers(src: list):
    """Возвращает элементы, значения которых больше предыдущего"""


    add = [b for a, b in zip(src, src[1:]) if a < b]
    return add


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(get_numbers(src))
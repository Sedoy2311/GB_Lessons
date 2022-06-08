def odd_nums(number: int) -> int:
    """Генератораторное выражение, возвращающее по очереди нечетные целые числа от 1 до number (включительно)"""


    gen = (j for j in range(1, n + 1, 2))
    return gen


n = 15
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
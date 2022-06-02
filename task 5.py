from random import randrange
import copy

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(arg, flag, **kwargs):
    """Функция возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)"""

    def rand(lst, flag):
        """Рандомайзер слов"""
        # Тернарный оператор
        return lst.pop(randrange(len(lst))) if flag and len(lst) else lst[randrange(len(lst))] if not flag else ''

    joke_list = []
    kwargs = copy.deepcopy(kwargs)
    for i in range(arg):
        joke = (' '.join([rand(value, flag) for value in kwargs.values()]))
        if joke.strip():
            joke_list.append(joke)
        else:
            return joke_list
    return joke_list

print(get_jokes(6, True, nouns=nouns, adverbs=adverbs, adjectives=adjectives))
print(get_jokes(6, False, nouns=nouns, adverbs=adverbs, adjectives=adjectives))
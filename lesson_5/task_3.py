tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Ибрагим', 'Мистер Твистер', 'Алёша']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    """Возвращает кортежи вида (<tutor>, <klass>)"""


    gen = ((tutors[i], klasses[i]) if len(klasses) > i else (tutors[i], None) for i in range(len(tutors)))
    return gen


generator = check_gen(tutors, klasses)
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
def thesaurus(*args) -> dict:
    """Создает словарь из имён сотрудников без повторения значений c учетом регистра"""

    dict_out = {}

    for name in args:
            name = name.capitalize()
            key = name[0]
            if key not in dict_out:
                dict_out[key] = []
            if name not in dict_out[key]:
                dict_out[key].append(name)
    return dict_out

print(thesaurus('Иван', 'иван', 'Мария', 'Петр', 'Илья', 'александр', 'ВАСИЛИЙ', 'ПЕТР'))
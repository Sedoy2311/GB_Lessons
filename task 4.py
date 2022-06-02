def thesaurus_adv(*args) -> dict:
    """Создает отсортированный словарь из имён и фамилий сотрудников без повторения значений c учетом регистра"""

    dict_out = {}
    for args in sorted(args):
        firstname, lastname = args.split(' ')
        firstname, lastname = firstname.capitalize(), lastname.capitalize()
        args = f'{firstname} {lastname}'
        keyval = dict_out.setdefault(lastname[0], {firstname[0]: [args]})
        subkeyval = keyval.setdefault(firstname[0], [args])
        if args not in subkeyval:
            subkeyval.append(args)
    return dict_out

print(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'игорь игнашевич', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева', 'АннА савельева', 'петр Модрич', 'Игорь Игнашевич'))
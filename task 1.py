def num_translate(value: str) -> str:
    """Переводит числительное с английского на русский от 1 до 10"""

    my_dict = {
'one': 'один',
'two': 'два',
'three': 'три',
'four': 'четыре',
'five': 'пять',
'six': 'шесть',
'seven': 'семь',
'eight': 'восемь',
'nine': 'девять',
'ten': 'десять'}

    str_out = my_dict.get(value)
    return str_out

print(num_translate('one'))
print(num_translate('eight'))
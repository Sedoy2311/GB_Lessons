def num_translate(value: str) -> str:
    """Переводит числительное с английского на русский от 1 до 10 c учетом регистра"""

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

    for i in my_dict:
        if value.istitle():
            value = value.lower()
            str_out = my_dict.get(value).capitalize()
        elif value.isupper():
            value = value.lower()
            str_out = my_dict.get(value).upper()
        else:
            value = value.lower()
            str_out = my_dict.get(value)
        return str_out

print(num_translate('zero'))
print(num_translate('one'))
print(num_translate('One'))
print(num_translate('ONE'))
print(num_translate('OnE'))
print(num_translate(input('Введите число на английском от 1 до 10: ')))
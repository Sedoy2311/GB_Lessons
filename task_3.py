import requests
import re
from datetime import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
r = response.text.replace(',', '.')

def currency_rates(code: str):
    """Возвращает курс валюты `code` по отношению к рублю и дату. Не чувствителен к регистру"""
    code = code.upper()
    date = datetime.strptime((re.search(r'\d{2}.\d{2}.\d{4}', r)).group(), '%d.%m.%Y').date()
    char = (' '.join(re.findall('<CharCode>([^<>]+)</CharCode>', r))).split()
    value = (' '.join(re.findall('<Value>([^<>]+)</Value>', r))).split()
    dict_code = dict(zip(char, value))
    return f'{code} = {round(float(dict_code.get(code)), 2)} руб, {date}' if code in dict_code else None
    # возвращает string для красоты, но сам курс числового типа float с округлением до сотых, а дата является объектом date

print(currency_rates('USD'))
print(currency_rates('EUr'))
print(currency_rates('noname'))
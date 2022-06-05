# С помощью модуля re
import requests
import re

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
r = response.text.replace(',', '.')

def currency_rates(code: str):
    """Возвращает курс валюты `code` по отношению к рублю. Не чувствителен к регистру"""
    code = code.upper()
    char = (' '.join(re.findall('<CharCode>([^<>]+)</CharCode>', r))).split()
    value = (' '.join(re.findall('<Value>([^<>]+)</Value>', r))).split()
    dict_code = dict(zip(char, value))
    return f'{code} = {float(dict_code.get(code))} руб' if code in dict_code else None

print(currency_rates('USD'))
print(currency_rates('EUr'))
print(currency_rates('noname'))

# С помощью модуля json
from requests import get, utils
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = get(url)
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
dict_json = json.loads(response.text)

def currency_rates(code: str):
    code = code.upper()
    return f'{code} = {dict_json["Valute"][code]["Value"]} руб' if code in content else None

print(currency_rates('Usd'))
print(currency_rates('eur'))
print(currency_rates('noname'))
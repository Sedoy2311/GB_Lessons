from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    for i in fr:
        addr = i.split(" - - ")[0]
        t_and_r = i.split('"')[1]
        typ = t_and_r.split()[0]
        resource = t_and_r.split()[1]
        yield addr, typ, resource


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    count = 0
    for _ in fr:
        count += 1
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for _ in range(count):
        list_out.append(next(get_parse_attrs(fr)))

pprint(list_out)
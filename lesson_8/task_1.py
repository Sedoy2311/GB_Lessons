import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile((r'^[a-zA-Z0-9_.+-]+'
                              r'@'
                             r'[a-zA-Z0-9-]{3,}\.[a-zA-Z0-9-.]{2,}$'))
    res_dict = {}
    try:
        if RE_MAIL.match(email):
            login, domain = email.split('@')
            res_dict['username'] = login
            res_dict['domain'] = domain
            return res_dict
        else:
            raise ValueError
    except ValueError:
        return print(f'ValueError: wrong email: {email}')


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
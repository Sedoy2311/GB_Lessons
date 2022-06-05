import sys
import utils
# Скрипт работает через консоль, в том числе с несколькими аргументами

args = sys.argv[1:]
for code in args:
    conv = utils.currency_rates(code)
    print(conv)
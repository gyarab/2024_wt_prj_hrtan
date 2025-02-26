import httpx
from datetime import datetime
import pygame as pg


current_date = datetime.today().strftime('%d.%m.%Y')
url = f'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date={current_date}'
blame = httpx.get(url).text


blame = blame.split('\n')
blame.pop()
for x in range(2):
    blame.pop(0)


exchange = {}
for line in blame:
    line = line.replace(',', '.')
    line = line.split('|')
    exchange[line[3]] = float(line[-1]) / float(line[2])

def start_rate():
    print('Which rate do you want to use?')
    for value in exchange.keys():
        print(f'{value}', end='\n')

    currency = ''
    while True:
        currency = input('Please type exactly what is written\n')
        try:
            if exchange[currency] is not None:
                break
            print('Type valid input')
        except:
            print('Type valid input')

    amount = 0
    while True:
        try:
            amount = float(input('Please type the amount of the rate you would like to use.\n'))
            if amount >= 0:
                break
            else:
                print('Type amount bigger or equal to zero.')
        except ValueError:
            print('Type valid input.')

    while True:
        way = input('Do you want from or to CZE?\n')
        if way == 'to':
            print(amount / exchange[currency])
            break
        elif way == 'from':
            print(amount * exchange[currency])
            break
        else:
            print('Type \"from\" or \"to\" for a valid input.')


start_rate()
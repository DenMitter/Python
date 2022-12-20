try:
    num = int(input('\nВведіть сумму: '))
    # print('\n* У рядку "Введіть валюту" можливо ввести тільки [USD],[AWG],[GEL]')
    # valute = input('Введіть валюту: ')
    for i in range(0, 1):
        print('\n---------------------------------')
        print(f'|\tUSA Dollar: {round(num*0.0269)}\t\t|')
        print(f'|\t   AWG: {round(num*0.04818)}\t\t|')
        print(f'|\t   GEL: {round(num*0.07068)}\t\t|')
        print('---------------------------------')
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
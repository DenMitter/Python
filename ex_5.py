try:
    num = int(input('Введіть кількість годин: '))

    if num > 0 < 6: print('Good Night')
    elif num > 6 < 13: print('«Good Day')
    elif num > 0 < 17: print('Good Night')
    else: print('Введіть корректне значення')

except Exception as ex:
    print('~~~~~~~~~~~~~~~ ERROR ~~~~~~~~~~~~~~~~~~~')
    print(f'{ex}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
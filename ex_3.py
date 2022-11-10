try:
    price = int(input('Введіть вартість однієї ігрової приставки: '))
    playses = int(input('Введіть ількість ігрових приставок: '))
    discount = int(input('Введіть їх знижку: '))
    all = playses * price // discount

    print('~~~~~~~~~~~~~~ Що виводимо ~~~~~~~~~~~~~~')
    print('|                                       |')
    print('|         Загальна вартість - A         |')
    print('|     Вартість однієї зі знижкою - O    |')
    print('|                                       |')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    to_end = input('Ваш вибір: ')

    if to_end == 'A' or to_end == 'a': print(f'Результат: {all}')
    else: print(f'Результат: площа - {area}, периметр - {price // discount}')

except Exception as ex:
    print('~~~~~~~~~~~~~~~ ERROR ~~~~~~~~~~~~~~~~~~~')
    print(f'{ex}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
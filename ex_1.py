try:
    num = int(input('Введіть секунди: '))
    hour = num // 3600
    min_sec = num % 3600
    minute = min_sec // 60
    sec = min_sec % 60
    day = 24 * 3600
    if num > day:
        raise Exception('У добі меньше секунд, введіть корректне значення')

    print('~~~~~~~ Скільки лишилось до кінця ~~~~~~~')
    print('|                                       |')
    print('|               Годин - H               |')
    print('|               Хвилин - M              |')
    print('|              Секунди - S              |')
    print('|     Години : Хвилини : Секунди - A    |')
    print('|                                       |')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    to_end = input('Ваш вибір: ')

    if to_end == 'H' or to_end == 'h': print(f'Залишилось: {24-hour} години')
    elif to_end == 'M' or to_end == 'm': print(f'Залишилось: {minute} хвилини')
    elif to_end == 'S' or to_end == 's': print(f'Залишилось: {sec*3600-24} секунд')
    else: print(f'Результат: {hour}:{minute}:{sec}')







except Exception as ex:
    print('~~~~~~~~~~~~~~~ ERROR ~~~~~~~~~~~~~~~~~~~')
    print(f'{ex}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')












#print('\n~~~~~~~ Скільки лишилось до кінця ~~~~~~~\n|\t\t\t\t\t\t\t\t\t\t|')
# print('|\t\t\tГодин\t-\tH\t\t\t\t|\n|\t\t\tХвилин\t-\tM\t\t\t\t|\n|\tГодини : Хвилини : Секунди\t-\tA\t|')
# print('|\t\t\t\t\t\t\t\t\t\t|\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
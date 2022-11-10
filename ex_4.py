try:
    num = int(input('Введіть розмір файлу в гігабайтах: '))
    speed = int(input('Введіть швидкість інтернет-з’єднання в бітах за секунду: '))
    hour = num // speed
    minute = hour * 60
    sec = minute * 60

    print('~~~~~~~~~~~~~~ Що виводимо ~~~~~~~~~~~~~~')
    print('|                                       |')
    print('|     Скільки знадобиться годин - H     |')
    print('|     Скільки знадобиться хвилин - M    |')
    print('|     Скільки знадобиться секунд - S    |')
    print('|                                       |')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    to_end = input('Ваш вибір: ')

    if to_end == 'H' or to_end == 'h': print(f'Залишилось: {hour} години')
    elif to_end == 'M' or to_end == 'm': print(f'Залишилось: {minute} хвилини')
    elif to_end == 'S' or to_end == 's': print(f'Залишилось: {sec*3600} секунд')
    else: print(f'Результат: {hour}:{minute}:{sec*3600}')

except Exception as ex:
    print('~~~~~~~~~~~~~~~ ERROR ~~~~~~~~~~~~~~~~~~~')
    print(f'{ex}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
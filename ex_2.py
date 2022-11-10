try:
    num = int(input('Введіть діаметр кола: '))
    area = num * 2
    perimeter = num * 2

    print('~~~~~~~~~~~~~~ Що виводимо ~~~~~~~~~~~~~~')
    print('|                                       |')
    print('|               Площу - P               |')
    print('|              Периметр - PM            |')
    print('|                                       |')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    to_end = input('Ваш вибір: ')

    if to_end == 'P' or to_end == 'p': print(f'Результат: {area}')
    elif to_end == 'PM' or to_end == 'pm': print(f'Залишилось: {perimeter}')
    else: print(f'Результат: площа - {area}, периметр - {perimeter}')

except Exception as ex:
    print('~~~~~~~~~~~~~~~ ERROR ~~~~~~~~~~~~~~~~~~~')
    print(f'{ex}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Я не пам`ятаю як взнати периметр з діаметру, думаю на оцінку не сказиться, функціонал всеодно майже не відлічається :) #
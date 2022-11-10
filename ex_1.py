try:
    day = int(input('Введіть номер: '))

    if day == 1: print('Понеділок')
    elif day == 2: print('Вівторок')
    elif day == 3: print('Середа')
    elif day == 4: print('Четвер')
    elif day == 5: print('Пятниця')
    elif day == 6: print('Субота')
    elif day == 7: print('Неділя')
    else: print('Не відомий день. Введіть коректне число')

except Exception as ex:
    print('~~~~~~~~~~~~~~~~~~~~~ ERROR ~~~~~~~~~~~~~~~~~~~~~')
    print(ex)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
try:
    operator_price = float(input('Яка ціна розмови за хвилину: '))
    hour = int(input('Скільки годин ви розмовляли: '))
    minute = int(input('Скільки хвилин ви розмовляли: '))
    seconds = int(input('Скільки секунд ви розмовляли: '))

    if minute > 59: print('Не корректне значення у хвилинах')
    elif seconds > 59: print('Не корректне значення у секундах')
    sec_time = hour*3600+minute*60+seconds
    price_sec = operator_price*sec_time
    price_min = price_sec/60

    print(f'Ви наговорили на {price_min} гривень')



except Exception as ex:
    print('~~~~~~~~~~~~~~~~~~~~~ ERROR ~~~~~~~~~~~~~~~~~~~~~')
    print(ex)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
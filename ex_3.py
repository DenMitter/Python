try:
    string = list(map(int,input('Введіть ряд чисел через пробіл: ').split()))
    symbol = int(input('Введіть символ для пошуку: '))
    num = 0

    for i in string:
        if i==symbol: num+=1

    print(f'Число {symbol} зустрічається {num} раз')

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
try:
    num = int(input('Введіть число: '))

    if num > 0: print('Number is positive')
    elif num < 0: print('Number is negative')
    elif num == 0: print('Number is equal to zero')
    else: print('Введіть коректне число')

except Exception as ex:
    print('~~~~~~~~~~~~~~~~~~~~~ ERROR ~~~~~~~~~~~~~~~~~~~~~')
    print(ex)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
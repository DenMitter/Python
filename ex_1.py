try:
    number = int(input('Введіть число від 1 до 100: '))

    if number % 3 == 0 and number % 5 != 0: print('Fizz')
    elif number % 5 == 0 and number % 3 != 0: print('Buzz')
    elif number % 3 == 0 and number % 5 == 0: print('Fizz Buzz')
    elif number > 0 and number < 100 and number % 3 != 0 and number % 5 != 0: print(number)
    else: print('Введіть корректне число')

except Exception as ex:
    print('~~~~~~~~~~~~~~~~~~~~~ ERROR ~~~~~~~~~~~~~~~~~~~~~')
    print(ex)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

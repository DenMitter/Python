try:
    num_one = int(input('Введіть перше число: '))
    num_two = int(input('Введіть друге число: '))

    if num_one == num_two: print('Числа рівні')
    elif num_one > num_two: print(f'{num_two}, {num_one}')
    else: print('Введіть коректне число')

except Exception as ex:
    print('~~~~~~~~~~~~~~~~~~~~~ ERROR ~~~~~~~~~~~~~~~~~~~~~')
    print(ex)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
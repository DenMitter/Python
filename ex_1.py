try:
    num_one = int(input('Введи перше число: '))
    num_two = int(input('Введи друге число: '))

    print(f'Результат: {num_one**num_two}')

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
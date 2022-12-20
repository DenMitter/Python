try:
    num = int(input('Введіть число: '))
    for i in range(1, 10):
        print(f'Результат: {num*i}')
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
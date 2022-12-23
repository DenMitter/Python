try:
    num = int(input('Введи число: '))

    for i in range(1, num+1):
        print(f'Результат: 7*{i}={num*i}')

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
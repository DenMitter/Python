try:
    num = int(input("Введіть число: "));

    for i in range(1, 10+1):
        for x in range(1, 10+1):
            print(f'{i} * {x} = {i*x}', end='\t\t')
        print()

        for x in range(1, 235):
            print('-', end='')
        print()
    print()

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
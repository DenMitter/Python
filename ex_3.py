try:
    num_one = int(input("Введіть число: "));
    num_two = int(input("Введіть число: "));

    for i in range(1, 10+1):
        for x in range(1, 10+1):
            if num_one == x:
                print(f'{i} * {x} = {i*x}', end='\t\t')
            elif num_two == x:
                print(f'{i} * {x} = {i*x}', end='\t\t')
            
        print()
    print()

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
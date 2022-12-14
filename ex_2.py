try:
    num = int(input('Number: '))
    factorial = 1

    for item in range(1, num+1):
        print(f'{factorial} * {item} = {factorial * item}', end='\t\n')
        factorial *= item

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
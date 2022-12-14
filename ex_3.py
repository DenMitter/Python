try:
    while True:
        num = int(input('\nВведіть число: '))
        if num == 7: 
            print('Good bye!')
            break
        elif num > 0: print('Number is positive')
        elif num < 0: print('Number is negative')
        elif num == 0: print('Number is equal to zero')

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
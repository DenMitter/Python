try:
    begin = int(input('begin->'))
    end = int(input('end->'))

    for item in range(begin, end+1):
        print(item, end='\t:')
        if item % 7 == 0: print('Число кратне 7')
        else: print('Число не кратне 7')

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
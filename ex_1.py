try:
    begin = int(input('begin->'))
    end = int(input('end->'))
    num = 0

    print('---------- Усі числа діапазону ----------')
    for item in range(begin, end+1):
        print(item, end='\t')

    print('\n\n--- Усі числа діапазону за спаданням ---')
    for item in range(end, begin-1, -1):
        print(item, end='\t')

    print('\n\n--------- Усі числа, кратні 7 ---------')
    for item in range(begin, end+1):
        print(item, end='\t:')
        if item % 7 == 0: print('Число кратне 7')
        else: print('Число не кратне 7')

    print('\n------ Кількість чисел, кратних 5 ------')
    for item in range(begin, end+1):
        if item % 5 == 0: num = num + 1 
    print(f'Усього {num} чисел кратних 5')

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
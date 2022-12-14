try:
    sum_ = 0
    min_ = 0
    max_ = 0
    while True:
        num = int(input('\nВведіть число: '))
        if num == 7: 
            print('Good bye!')
            break
        else: 
            sum_ += num
            if max_ < num: max_ = num
            if min_ > num: min_ = num
    print(f'\nSum = {sum_}')
    print(f'Min = {min_}')
    print(f'Max = {max_}')

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
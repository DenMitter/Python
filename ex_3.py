try:
    start = int(input('\nВведіть початок діапазону: '))
    end = int(input('\nВведіть цінець діапазону: '))
    num = int(input('\nВведіть число: '))

    if num > end or num < start:
        while num > start and num < end:  
            num = int(input('\nВведіть число яке потрапляє в діапазон: '))

    for i in range(start, end):
        print(i)
        if i == num: print(f'!{num}!')

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
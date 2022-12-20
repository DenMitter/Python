try:
    start = int(input('\nВведіть початок діапазону: '))
    end = int(input('\nВведіть цінець діапазону: '))

    if start > end: 
        start, end = end, start

    while True:
        num = int(input('\nВведіть число: '))
        if start <= num and num <= end:
            for i in range(start, end+1):
                if i < num or i > num: print(i, end=" ")
                else: print(f'!{i}!', end=" ")
            break
        else: 
            print('Число не входить у діапазон')

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
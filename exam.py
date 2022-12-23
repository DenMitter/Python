try:
    start = int(input('\nВведіть початок: '))
    end = int(input('\nВведіть кінець: '))
    if start > end: 
        end, start = start, 
    if start < -100000 or end > 100000:
        print('Введіть число не меньше ніж -100000 і не більше ніж 100000')

    for i in range(start, end):
        if i % 3 == 0 or i % 7 == 0: continue
        print(i)

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
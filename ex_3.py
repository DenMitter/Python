num_one = int(input('Введіть перше число: '))
num_two = int(input('Введіть друге число: '))

if num_one < num_two:
    print(f'Результат: {num_two}')
elif num_one > num_two:
    print(f'Результат: {num_one}')
else:
    print(f'Результат: {num_one} = {num_two}')
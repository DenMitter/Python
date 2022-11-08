num_one = int(input('Введіть перше число: '))
num_two = int(input('Введіть друге число: '))
action = int(input('Що виводимо ( меньше 1 | більше 2 | середнє 3 ): '))

if action == 1:
    if num_one < num_two:
        print(f'Результат: {num_one}')
    else:
        print(f'Результат: {num_two}')
elif action == 2:
    if num_one > num_two:
        print(f'Результат: {num_two}')
    else:
        print(f'Результат: {num_one}')
else:
    print(f'Результат: {num_one} = {num_two}')















# if num_one < num_two:
#     print(f'Результат: {num_one} < {num_two}')
# elif num_one > num_two:
#     print(f'Результат: {num_one} > {num_two}')
# else:
#     print(f'Результат: {num_one} = {num_two}')
num_one = int(input('Введіть перше число: '))
num_two = int(input('Введіть друге число: '))
num_three = int(input('Введіть третє число: '))
action = int(input('Що робимо ( множити 1 | додати 2 ): '))

if action == 1: print(f'Результат: {num_one * num_two * num_three}')
else: print(f'Результат: {num_one + num_two + num_three}')
num_one = int(input('Введіть перше число: '))
num_two = int(input('Введіть друге число: '))
action = int(input('Що робимо ( множити 1 | відняти 2 | додати 3 | avg 4): '))

if action == 1: print(f'Результат: {num_one * num_two}')
elif action == 2: print(f'Результат: {num_one - num_two}')
elif action == 3: print(f'Результат: {num_one + num_two}')
elif action == 4: print(f'Результат: {num_one + num_two / 2}')
else: print('Command not found')

num_one = int(input('Введіть довжину у метрах: '))
action = int(input('У що конвертувати ( милі 1 | дюйми 2 | ярди 3 ): '))

if action == 1: print(f'Результат у милях: {num_one * 0.000621371}')
elif action == 2: print(f'Результат у дюймах: {num_one * 39.3701}')
else: print(f'Результат у ярдах: {num_one * 1.09361}')
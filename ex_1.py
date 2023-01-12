try:
    num_one = int(input("Введіть початок: "));
    num_two = int(input("Введіть кінець: "));

    if num_one > num_two:
        num_one, num_two = num_two, num_one

    for i in range(num_one, num_two):
        if i % i == 0 and i % 1 == 0:
            print(i)
        continue

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
try:
    num_one = int(input("Введіть початок: "));
    num_two = int(input("Введіть кінець: "));

    if num_one > num_two:
        num_one, num_two = num_two, num_one

    for i in range(num_one, num_two+1):
        counter = 0
        for x in range(1, i+1):
            if i % x == 0:
                counter += 1
        if counter == 2:
            print(i, end=' ')
    print()

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
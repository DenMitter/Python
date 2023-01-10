try:
    num_one = int(input("Введіть ширину прямокутника: "));
    num_two = int(input("Введіть висоту прямокутника: "));

    for i in range(0, num_one):
        for x in range(0, num_two):
            if i == 0 or i == num_one-1: 
                print("*", end=' ')
            else: 
                if x == 0 or x == num_two-1: 
                    print("*", end=' ')
                else:
                    print(" ", end=' ')
        print()

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
try:
    num = int(input("Введіть розмір квадрата: "));

    for i in range(0, num):
        for x in range(0, num):
            if i == 0 or i == num-1: 
                print("*", end=' ')
            else: 
                if x == 0 or x == num-1: 
                    print("*", end=' ')
                else:
                    print(" ", end=' ')
        print()

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
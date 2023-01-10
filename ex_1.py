try:
    num = int(input("Введіть сторони квадрата: "));

    for i in range(0, num):
        for x in range(1, num):
            print("*", end='\t')
        print("*")

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
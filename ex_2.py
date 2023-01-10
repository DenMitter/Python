try:
    num_one = int(input("Введіть ширину прямокутника: "));
    num_two = int(input("Введіть висоту прямокутника: "));

    for i in range(0, num_two):
        for x in range(1, num_one):
            print("*", end='\t')
        print("*")

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
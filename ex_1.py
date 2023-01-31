import random
try:
    length = int(input("Введіть кількість елементів у списках: "))
    choice = int(input("1) Елементи обох списків \n2) Елементи обох списків без повторень \n3) Елементи, спільні для двох списків \n4) Тільки унікальні елементи кожного зі списків \n5) Усе вище \n Введіть свій вибір:"))
    list1 = []
    list2 = []

    if length > 0:
        for i in range(length):
            list1.append(random.randint(0, 100))
            list2.append(random.randint(0, 100))

        print("Список 1: ", list1)
        print("Список 2: ", list2)

        if choice == 1 or choice == 5:
            list3 = list1 + list2
            print("Елементи обох списків: ", list3)

        if choice == 2 or choice == 5:
            list3 = list(set(list1 + list2))
            print("Елементи обох списків без повторів: ", list3)

        if choice == 3 or choice == 5:
            list3 = list(set(list1) & set(list2))
            print("Елементи, спільні для двох списків: ", list3)

        if choice == 4 or choice == 5:
            list3 = list(set(list1) ^ set(list2))
            print("Тільки унікальні елементи кожного зі списків: ", list3)

    else:
        print("Елементи в списках мають бути додатними")
    

except Exception as ex:
    print(f"Error: [{ex.__class__.__name__}]: {ex}")
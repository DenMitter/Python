try:
    operation = input("operation-> ")
    parts = operation.split()
    operation_one = 0

    if parts[1] == "+":
         operation_one = int(parts[0]) + int(parts[2])

    elif parts[1] == "*":
        operation_one = int(parts[0]) * int(parts[2])

    elif parts[1] == "-":
         operation_one = int(parts[0]) - int(parts[2])

    elif parts[1] == "/":
         operation_one = round(int(parts[0]) / int(parts[2]))

    print(operation_one)
    

except Exception as ex:
    print(f"Error: [{ex.__class__.__name__}]: {ex}")
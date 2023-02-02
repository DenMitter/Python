import random

try:
    lengthOflist = int(input('Length of list->'))
    begin = int(input('begin->'))
    end = int(input('end->'))
    zero, positive, negative = 0, 0, 0

    if begin > end:
        begin, end = end, begin
    numbers = list()
    
    for i in range(0, lengthOflist):
        numbers.append(random.randint(begin, end))
        if numbers[i] == 0: zero += 1
        elif numbers[i] > 0: positive += 1
        elif numbers[i] < 0: negative += 1
    print(numbers)

    print(f'max-> {max(numbers)}\nmin-> {min(numbers)}')
    print ("\nzero->", zero, "\npositive->", positive, "\nnegative->", negative)
    

except Exception as ex:
    print(f"Error: [{ex.__class__.__name__}]: {ex}")
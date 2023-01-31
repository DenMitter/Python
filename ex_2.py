import random
try:
    #----------------------------------------------#
    lengthOflist = int(input('Length of list->'))
    begin = int(input('begin->'))
    end = int(input('end->'))
    if begin > end:
        begin, end = end, begin
    numbers = list()
    for i in range(0, lengthOflist):
        numbers.append(random.randint(begin, end))
    print(numbers)
    #----------------------------------------------#

    sum_neg = 0
    for num in numbers:
        if num < 0:
            sum_neg += 1
    print('negative-> ', sum_neg)

    sum_pos = 0
    for num in numbers:
        if num < 0:
            sum_neg += 1
    print('positive-> ', sum_neg)

    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += 1
    print('even-> ', sum_even)

    sum_odd = 0
    for num in numbers:
        if num % 2 != 0:
            sum_odd += 1
    print('odd-> ', sum_odd)
    

except Exception as ex:
    print(f"Error: [{ex.__class__.__name__}]: {ex}")
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
            sum_neg += num
    print('sum negative-> ', sum_neg)

    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    print('sum even-> ', sum_even)

    sum_odd = 0
    for num in numbers:
        if num % 2 != 0:
            sum_odd += num
    print('sum odd-> ', sum_odd)

    indices_three = 1
    for i, num in enumerate(numbers):
        if i % 3 == 0:
            indices_three *= num
    print('indices that are multiples of 3-> ', indices_three)

    prod_min_max = 1
    min_num = min(numbers)
    max_num = max(numbers)

    for num in numbers:
        if num > min_num and num < max_num:
            prod_min_max *= num
    print('min or max-> ', prod_min_max)

    sum_pos = 0
    first_found = False
    last_found = False

    for num in numbers:
        if num > 0 and first_found == False:
            first_found = True

        elif first_found == True and num > 0:
            sum_pos += num

        elif first_found == True and num < 0:
            last_found = True

        if last_found == True and num > 0:
            break

    print('sum pos-> ', sum_pos)
    

except Exception as ex:
    print(f"Error: [{ex.__class__.__name__}]: {ex}")
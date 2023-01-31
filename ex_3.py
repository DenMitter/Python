import random

try:
    lengthOflist = int(input('Length of list->'))
    begin = int(input('begin->'))
    end = int(input('end->'))
    if begin > end:
        begin, end = end, begin
    numbers = list()
    for i in range(0, lengthOflist):
        numbers.append(random.randint(begin, end))
    print(numbers)

    partList = numbers[numbers.index(max(numbers))+1: numbers.index(min(numbers))].copy()
    print(partList)
    mul = 1
    for item in partList:
        mul *= item
    print(mul)
    

except Exception as ex:
    print(f"Error: [{ex.__class__.__name__}]: {ex}")
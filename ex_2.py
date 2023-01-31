import random

try:
    lengthOflist = int(input('Length of list-> '))
    begin = int(input('begin-> '))
    end = int(input('end-> '))
    num = int(input('number-> '))
    if begin > end:
        begin, end = end, begin
    numbers = list()
    for i in range(0, lengthOflist):
        numbers.append(random.randint(begin, end))
    print(numbers)

    print(numbers.count(num))
    

except Exception as ex:
    print(f"Error: [{ex.__class__.__name__}]: {ex}")
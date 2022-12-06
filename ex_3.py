try:
    begin = int(input('begin->'))
    end = int(input('end->'))
    
    for item in range(begin, end+1):
        print(item, end='\t:')
        if item % 5 == 0: print('Fizz')
        elif item % 3 == 0: print('Buzz')
        elif item % 5 == 0 and item % 3 == 0: print('Fizz Buzz') #Чомусь не працює
        else: print(item)

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
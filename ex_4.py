try:
    length = int(input('length->'))
    symbol = input('symbol->')

    for item in range(0, length):
        print(symbol, end='')

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
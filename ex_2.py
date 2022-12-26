try:   
    count = 0
    for i in range(100, 1000):
        digits = [int(d) for d in str(i)]
        filtered_digits = [d for d in digits if digits.count(d) > 1]

        if len(filtered_digits) > 1: count += 1
    print(count)

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
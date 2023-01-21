try:
    string = input('Введіть текст: ')
    letter_count = 0
    digit_count = 0

    for char in string:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1

    print('Кількість літер:', letter_count)
    print('Кількість цифр:', digit_count)

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
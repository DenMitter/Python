try:
    text = input("Введіть текст: ")
    result = text[::-1]
    print(result)

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
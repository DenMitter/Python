try:
    text = input("Введіть слово: ")
    pali = text[::-1]
    if text != pali: print("Ви вказали не паліндром слово");
    else: print(text)

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
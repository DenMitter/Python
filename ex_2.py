try:
    text = input("Введіть текст: ")
    find = input("Введіть символ для пошуку: ")
    len_text = len(text)
    print(f'Кількість літер: {len_text}\nКількість найдених символів: {text.find(find, 0)}')

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
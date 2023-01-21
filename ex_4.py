try:
    original_string = input("Введіть текст: ")
    word_to_replace = input("Введіть слово для пошуку: ")
    modified_string = original_string.find(word_to_replace)

    print("Готова строка: " + modified_string)

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
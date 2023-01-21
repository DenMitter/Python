try:
    original_string = input("Введіть текст: ")
    word_to_replace = input("Введіть слово для пошуку: ")
    replacement_word = input("Введіть слово для заміни: ")
    modified_string = original_string.replace(word_to_replace, replacement_word)

    print("Готова строка: " + modified_string)

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
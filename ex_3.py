try:
    text = input("Введіть текст: ")
    num_sentences = text.count('.') + text.count('!') + text.count('?')

    print(f"Кількість пропозицій у тексті: {num_sentences}")

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
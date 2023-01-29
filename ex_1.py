import string

try:
    #Num 1
    text = "певний текст".capitalize()
    print(text)

    #Num 2
    text = "Певний текст #1"
    num = sum(i.isnumeric() for i in text)
    result = len(text) - num

    print(f'Цифр у тексті: {num}')

    #Num 3
    text = "Певний текст. IT Step - IT Шаг"
    num = 0

    for i in text:
        if i in string.punctuation:
            num += 1
    print(f'Розділових знаків: {num}')

    #Num 4
    text = "Певний текст!".count("!")
    print(f'Знаків оклику: {text}')

except Exception as ex:
    print(f"Error: [{ex.__class__.__name__}]: {ex}")
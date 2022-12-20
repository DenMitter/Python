import random
try:
    guesses_made = 0
    number = random.randint(1, 500)
    print ('Я загадав число між 1 и 500. Зможеш вгадати?')

    while guesses_made < 6:
        guess = int(input('Введи число: '))
        guesses_made += 1

        if guess < number: print ('Твоє число меньше того, що я загадав.')
        if guess > number: print ('Твоє число більше загаданного мною.')
        if guess == number: break

    if guess == number:
        print (f'Ти вгадав моє число, викароситав {guesses_made} спроб!')
    else:
        print (f'А ось і не вгадав! Я загадав число {number}')

except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
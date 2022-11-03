int_one = int(input("Введіть ціле число: "))
EOS = 0
 
while int_one > 0:
    digit = int_one % 10
    int_one = int_one // 10
    EOS = EOS * 10
    EOS = EOS + digit  
 
print('Результат:', EOS)
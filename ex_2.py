int_one = int(input("Введіть число: "))
resault = []
while int_one:
    resault.append(int_one % 10)
    int_one //= 10
print(*resault[::-1], sep='\n')

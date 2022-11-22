number = int(input("Введіть число: "))
st = int(input("Введіть степінь від 0 до 7:"))

if st > 7 or st < 0: print("Степінь має бути від 0 до 7")
else: print(number**st)
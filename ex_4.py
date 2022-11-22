manager_one = int(input('\nВведіть сумму продажу першого менеджера: '))
manager_two = int(input('Введіть сумму продажу другого менеджера: '))
manager_three = int(input('Введіть сумму продажу третього менеджера: '))
price = 200

if manager_one > 1000: payroll_one = price+manager_one*0.08
else:
    if manager_one < 500: payroll_one = price+manager_one*0.03
    else: payroll_one = price+manager_one*0.05

if manager_two > 1000: payroll_two = price+manager_two*0.08
else:
    if manager_two < 500: payroll_two = price+manager_two*0.03
    else: payroll_two = price+manager_two*0.05

if manager_three > 1000: payroll_three = price+manager_three*0.08
else:
    if manager_three < 500: payroll_three = price+manager_three*0.03
    else: payroll_three = price+manager_three*0.05

if payroll_one > payroll_two and payroll_one > payroll_three: 
    print('Кращий по продажу - 1 менеджер!')
    payroll_one += 200

if payroll_two > payroll_one and payroll_two > payroll_three: 
    print('Кращий по продажам - 2 менеджер!')
    payroll_two += 200

if payroll_three > payroll_one and payroll_three > payroll_two: 
    print('Кращий по продажам - 3 менеджер!')
    payroll_three +=200

print('\nЗарплата 1 менеджера: ',payroll_one)
print('Зарплата 2 менеджера: ',payroll_two)
print('Зарплата 3 менеджера: ',payroll_three)
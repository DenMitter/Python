meters = int(input('Введіть довжину у метрах: '))
resault_sunt = meters*100
resault_mm = meters*1000
resault_dm = meters*10
resault_mile = meters*0.000621371

print('\n~~~~~~~~~~~~~~~~~~~~ [ Конвертація ] ~~~~~~~~~~~~~~~~~~~~')
print(f'\
Результат у сантиметрах: {resault_sunt}\n\
Результат у міліметрах: {resault_mm}\n\
Результат у децеметрах: {resault_dm}\n\
Результат у милях: {resault_mile}'
)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
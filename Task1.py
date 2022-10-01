# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
float_number = (input('введите вещественное число '))
lenght = len(float_number)
sum_float_number = 0
for i in range(lenght):
    if float_number[i] != '.':
        sum_float_number += int(float_number[i])
print(f'сумма цифр в числе {float_number} равна {sum_float_number}')






# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

N = int(input('введите число '))
dict = { }
for i in range(1 , N+1):
    sum = 0
    for j in range(1 , i+1):
        sum = sum + round((1 + 1 / j)**j , 0)
    dict[i] = {sum}
print(dict)

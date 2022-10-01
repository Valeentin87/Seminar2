# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
N = int(input("введите число "))
result = ' '
for i in range(1 , N+1):
    composition = 1
    for j in range(1, i+1):
        composition = composition*j
    result = result + str(composition) + ','
print(f'[ {result} ]')
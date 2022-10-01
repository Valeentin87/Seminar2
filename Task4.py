# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. \
# Найдите произведение элементов на указанных позициях. \
# Позиции хранятся в файле file.txt в одной строке одно число.
import random
N = int(input('введите число элементов в последовательности'))
lst = [None]*N
for i in range(0, N):
    lst[i] = random.randint(-N, N)
print(lst)
if N%2==0:
    result_numbers = N/2
else:
    result_numbers = N//2 +1
res_lst = [None]*result_numbers
j = 0
for i in range(result_numbers):
    res_lst[i] = lst[i]*lst[j-1]
    j = j-1
print(res_lst)




# Реализуйте алгоритм перемешивания списка.
import random
N = int(input('введите число элементов в последовательности'))
lst = [None]*N
for i in range(0, N):
    lst[i] = random.randint(-N, N)
print(lst)
res_lst = [None]*N
left_index = 0
right_index = N-1
replacement = 0
while(left_index<=right_index):
    replacement = lst[left_index]
    res_lst[left_index] = lst[right_index]
    res_lst[right_index] = replacement
    left_index += 1
    right_index = right_index - 1
print(res_lst)
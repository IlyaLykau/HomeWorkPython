# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

n = int(input('введите количество элементов массива: '))
lst_1 = []

for i in range(n):
    num = int(input('введите число: '))
    lst_1.append(num)
    print(lst_1)

X = int(input('введите число для сравнения: '))
print(f'{X} встречается в массиве: {lst_1.count(X)}') 
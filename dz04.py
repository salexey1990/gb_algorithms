# 1

# вывести наибольший отрицательный элемент масссива

x = [1, 2, 3, -1, -2, -3, -2]

# 1 шаг - отфильтровать все отрицательные элементы массива.
# включает один проход по массиву, выполняется за О(n)

less_than_zero = list(filter(lambda x: x < 0, x))

# 2 шаг - сортировка оставшихся отрицательных элементов массива
# встроенный в питон алгоритм сортировки выполняется за
# Best Case Performance : O(n)

# Average Case Performance : O(nlogn)

# Worst Case Performance : O(nlogn)

less_than_zero.sort()

# 3 шаг - взятие последнего элемента массива
# последний элемент массива, как и любой другой доступен за О(1)

print(less_than_zero[-1])


# 2

n = int(input())
numbers = list(range(2, n + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, n+1, number):
            numbers[candidate-2] = 0    
print(*list(filter(lambda x: x != 0, numbers)))

n = int(input())
numbers = list(range(2, n + 1))
res = []
has_divider = False
for number in numbers:
    for i in range(2, number):
        if not number % i:
            has_divider = True
    if not has_divider:
        res.append(number)
    else:
        has_divider = False

print(res)
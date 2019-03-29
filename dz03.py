# 1

# res = {}

# for i in range(2,10):
#   res[i] = 0

# for i in range(1000000):
#   for j in range (2,10):
#     if not i % j:
#       res[j] +=1

# print(res)

# 2

# a = [8, 3, 15, 6, 4, 2]

# res = []

# for i, number in enumerate(a):
#   if not number % 2:
#     res.append(i)

# print(res)

# 3

# seq = [7, 4, 0, 3, 8, 6, 5, 1, 2, 9]

# min_indx = seq.index(min(seq))
# max_indx = seq.index(max(seq))

# seq[min_indx], seq[max_indx] = seq[max_indx], seq[min_indx]

# print(seq)

# 4

import random

# x = [int(100*random.random()) for i in range(10000)]

# y = {}

# for i in x:
#   if i in y:
#     y[i] +=1
#   else:
#     y[i] = 0

# val = 0
# k = 0

# for key, value in y.items():
#   if value > val:
#     val = value
#     k = key

# print(k)

# 5

# x = [1, 2, 3, -1, -2, -3, -2]

# less_than_zero = list(filter(lambda x: x < 0, x))

# less_than_zero.sort()

# print(less_than_zero[-1])

# 6

# x = [int(100*random.random()) for i in range(10)]

# x.sort()

# print(sum(x[1:-1]))

# 7

# x = [int(100*random.random()) for i in range(10)]

# x.sort()

# print(x[0], x[1])

# 8

# x = input()
# y = input()
# z = input()

# matr = []

# x = x.split(' ')
# x = list(map(int, x))
# x.append(sum(x))
# matr.append(x)

# y = y.split(' ')
# y = list(map(int, y))
# y.append(sum(y))
# matr.append(y)

# z = z.split(' ')
# z = list(map(int, z))
# z.append(sum(z))
# matr.append(z)

# print(matr)

# 9

# matr = [[1,2,3],[5,4,3],[5,6,7]]

# col = {}

# for i in range(len(matr)):
#     for j in range(len(matr[i])):
#       if not j in col:
#         col[j] = matr[i][j]
#       else:
#         if matr[i][j] < col[j]:
#           col[j] = matr[i][j]

# val = col[0]

# for key, value in col.items():
#   if value > val:
#     val = value

# print(val)


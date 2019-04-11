import sys


numbers = [1, -0.5, 0.25, -0.125]

# print('numbers', sys.getsizeof(numbers)) -->> ('numbers', 104)

n = int(input('input n: '))

# print('n', sys.getsizeof(n)) -->> ('n', 24)

if 1 <= n <= len(numbers):
  res = 0

  # print('res', sys.getsizeof(res)) -->> ('res', 24)

  # print('range(n)', sys.getsizeof(range(n))) -->> ('range(n)', 96)
  for i in range(n):
    res += numbers[i]

  print(res)
else:
  print('wrong params')

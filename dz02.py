# 1

# def add(x, y):
#   print(x + y)

# def subtract(x, y):
#   print(x - y)

# def multiply(x, y):
#   print(x  * y)

# def divide(x, y):
#   if y == 0:
#     print('wrong params')
#     return
#   print(x / y)

# menu = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# while True:

#   for key in list(menu.keys()):
#     print(f"{key}")

#   x = int(input('first number: '))
#   y = int(input('second number: '))

#   command = input("Input command: ")

#   if command == '0':
#     exit()
#   elif command not in list(menu.keys()):
#     print('wrong command')
#     continue
  
#   menu[command](x, y)

# 2

# number = input('input a number: ')

# even_count = 0
# odd_count = 0

# for i in number:
#   if int(i) % 2:
#     odd_count += 1
#   else:
#     even_count += 1

# print(f"odd count = {odd_count}, even count = {even_count}")

# 3

# x = input('input number: ')
# print(x[::-1])

# 4

# numbers = [1, -0.5, 0.25, -0.125]

# n = int(input('input n: '))

# if 1 <= n <= len(numbers):
#   res = 0

#   for i in range(n):
#     res += numbers[i]

#   print(res)
# else:
#   print('wrong params')

# 5

# codes = list(range(32, 128))

# table = [[]]
# row = 0

# for i, code in enumerate(codes):
#   if not (i % 10) and i != 0:
#     print(table[row])
#     row +=1
#     table.append([])

#   table[row].append((code, chr(code)))

# print(table[row])

# 6

import random

# number = random.randint(0, 100)

# for i in range(10):
#   x = int(input('input number: '))
#   if x == number:
#     print('you win!')
#     exit()
#   elif x > number:
#     print('>')
#   else:
#     print('<')
# print('you lose')

# 7

from functools import reduce

# n = random.randint(0, 100)

# print(reduce(lambda a, b : a + b, range(0, n + 1)) == n * (n + 1) / 2)

# 8

# sequence = input('input a sequence: ')
# x = input('input x: ')

# count = 0

# for i in sequence:
#   if i == x:
#     count +=1

# print(count)

# 9

# x = input()
# y = input()

# def my_sum(number):
#   return reduce(lambda a, b : int(a) + int(b), number)

# x_sum = my_sum(x)
# y_sum = my_sum(y)

# if x_sum > my_sum(y):
#   print(x, x_sum)
# else:
#   print(y, y_sum)


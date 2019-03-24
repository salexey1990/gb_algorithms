# 1
# a = input('input number: ')

# if len(a) != 3:
#   print('wrong input!')
#   exit()


# b = 0
# c = 1

# for i in a:
#   b += int(i)
#   c *= int(i)

# print(b)
# print(c)

# 2

# a = 5
# b = 6

# c = a & b
# d = a | b
# e = a ^ b
# f =  ~ a
# g = a >> 2
# h = a << 2

# print(a,b,c,d,e,f,g,h)

# 3

# a = input('input a: ')
# b = input('input b: ')
# k = int(a[1]) - int(b[1])
# d = int(a[0]) * int(b[1]) - int(b[0]) * int(a[1])
# c = int(b[0]) - int(a[0])

# print('y = ', k/-c, 'x + ', d/-c)

# 4

# import random

# a

# a = input()

# print(random.randrange(int(a[0]), int(a[1])))

# b

# a = input()

# print(random.uniform(int(a[0]), int(a[1])))

# c

# a = input()

# print(chr(random.randrange(ord(a[0]), ord(a[1]))))

# 5

# a = input()

# print('1 - ', ord(a[0]) - 96, '2 - ', ord(a[1]) - 96, 'между ними ', ord(a[1]) - ord(a[0]) - 1)

# 6

# a = input()

# print(chr(int(a) + 96))

# 7

# a = int(input())
# b = int(input())
# c = int(input())
 
# if a + b <= c or a + c <= b or b + c <= a:
#   print('Треугольник не существуе')
# elif a != b and a != c and b != c:
#   print('Разносторонний')
# elif a == b == c:
#   print('Равносторонний')
# else:
#   print('Равнобедренный')

# 8

# a = int(input())

# if a % 4 != 0 or (a % 100 == 0 and a % 400 != 0):
#   print('обычный')
# else:
#   print('високосный')

# 9

# a = int(input())
# b = int(input())
# c = int(input())

# d = [a,b,c]
# d.sort()

# print(d[1])
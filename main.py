# 1
# a = int(input("Введите число А:"))
# b = int(input("Введите число Б >= А:"))
# if a > b:
#     print("Неправльное число")
# for i in range(a,b + 1):
#     print(i)

# 2
# a = int(input("Введите число А:"))
# b = int(input("Введите число Б:"))
# if a < b:
#     for i in range(a, b + 1):
#         print(i, end=' ')
# else:
#     for i in range(a, b - 1, -1):
#         print(i, end=' ')

# 3
# sum = 0
# n = int(input())
# for i in range(1, n + 1):
# 	sum += i
# print(sum)

# 4
# n = int(input())
# factorial = n
# for i in range(1, n):
#     factorial *= i
# print(factorial)

# 5
# n = int(input())
# if n > 9:
#     print("Неправильное число")
# else:
#     for i in range(n):
#         print(end="\n")
#         for i in range(1, i + 2):
#             print(i, end="")

# 6
# n = int(input())
# x = 1
# while x ** 2 < n:
#     print(x, x ** 2)
#     x += 1

# 7
# n = int(input())
# st = 1
# k = 1
# p = 1
# while k < n:
#     for i in range(st):
#         p *= 2
#     k = p
#
#     print(k)
#     p = 1
# print(st)

# 8
# x = int(input())
# y = int(input())
# l = x
# d = 1
#
# while l <= y:
#     l += 0.1 * l
#     d += 1
# print(d)
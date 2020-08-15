# 2020.8.15
# 
# “杨辉三角形”是二项式系数的一种写法，形似三角形，
# 因为首现于南宋杨辉撰写的《详解九章算法》而得名，
# 它从第0行到第4行规则如下图所示。
# 请使用Python3编程，打印出“杨辉三角形”的前十行。

# 理解错误！
# for i in range(1, 11):
#     L = i
#     LST = []
#     if L <= 2:
#         for i in range(L):
#             LST.append(1)
#         print(LST.center(11))
#     else:
#         for i in range(L):
#             if i == 0 or i == L-1:
#                 LST.append(1)
#             else:
#                 LST.append(0)
#         print(LST)

old_line = []
n = 10

for i in range(1, n+1): 
    new_line = [1] * i
    for j in range(2, i): # range(2, 1)、range(2, 2)都不会执行，range(2, 3才会执行j = 2)
        index = j - 1
        new_line[index] = old_line[index] + old_line[index - 1]
    old_line = new_line
    print(new_line)


# 今天我学习了约瑟夫环的问题。
# 约瑟夫环是一个经常出现在计算机科学和数学中的问题，并不难，
# 题目的变化形式很多，求解的方法也很多。
# 比如，用约瑟夫环解决报数的问题：有n个人围成一圈，顺序排号。
# 从第一个人从1到3开始报数，报到3的人退出，
# 问最后留下的是最初的几号？
# 请用Python3编写程序解决这个问题。

# 我理解， 按1-3报数，报到3的人退出，只做一次。。。其实是一直做下去，。。。
n = int(input("几个人？"))
k = int(input("按多少报数？"))

l_1 = []


for i in range(1, n+1):
    l_1.append(i)
print(l_1)

# for  j in range(0, n, k):
#     print("..")
#     print(j)
#     for p in range(k):
#         m = j + p
#         print(m)
#         if m < n and p != k - 1: # and 和 or 按先后顺序执行？？
#             l_2.append(l_1[j+p])
# print(l_2)


def split(lst_1, k):
    n = len(lst_1)
    t_1 = n // k
    lst_2 = lst_1[:t_1 * k ] # 取出前面的数（按模）
    lst_3 = lst_1[t_1 * k :]
    return lst_2, lst_3

# 取模后，弹出数到的人
def pop(lst_1, k):
    lst_2 = []
    for i in range(len(lst_1)):
        if (i + 1) % k == 0:
            pass
        else:
            lst_2.append(lst_1[i])
    return lst_2

while len(l_1) != 1:
    if len(l_1) >= k:
        a, b = split(l_1, k)
        print(a)
        print(b)

        c = pop(a, k)
        print(c)

        l_1 = b + c
        print(l_1)
    else:
        l_1.pop(k % len(l_1) - 1)

print(l_1)



# 请用Python3语言，求一个3*3矩阵主对角线元素之和。

jz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = 0

# for i in range(0, 3):
for i in range(3):
    # s = s + jz[i][i]
    s += jz[i][i]

print(s)
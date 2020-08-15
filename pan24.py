# 请用Python3编程，对10个数进行倒序排序（不能使用sort函数）。

n_1 = []
for i in range(0, 10):
    n = float(input("number: "))
    n_1.append(n)

for j in range(0, 10):
    for k in range(j+1, 10):
        if n_1[j] < n_1[k]:
            n_1[j], n_1[k] = n_1[k], n_1[j]

print(n_1)
# 请输入一个奇数，
# 打印出一个行数为奇数行的菱形，
# 如下图就是行数为7的菱形。

while True:
    n = int(input())
    if n % 2 == 0:
        print("try again!")
    else:
        break

s = 1
for i in range(1, n + 1):
    k = int((n + 1)/2)
    if i < k:
        print(" " * (k - i), "*" * s)
        s = s + 2
    else:
        print(" " * (i - k), "*" * s)
        s = s - 2

# method 2 from pan:
n = int(input())

for i in range(1, n + 1, 2): # 递增2
    s = "*" * i
    print(s.center(n))
for i in range(n - 2, 0, -2):
    s = "*" * i
    print(s.center(n))
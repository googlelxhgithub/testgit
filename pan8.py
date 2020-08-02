# 水仙花数（Narcissistic number）是指一个三位数，
# 它的每个位上的数字的3次幂之和等于它本身。
# 水仙花数是自幂数的一种。
# 通过计算水仙花数可以练习编程水平。问题：如何求出所有三位正整数中的水仙花数？

print("method 1: what i do")
flower =  []

for n in range(100, 1000):
    # 求出百位数
    a = n//100
    # 计算10位数
    b = (n - a*100)//10
    # 计算个位数
    c = n-a*100-b*10
    # 如果条件成立，就记录到list里面
    if a ** 3 + b ** 3 + c ** 3 == n:
        flower.append(n)
    # n = n + 1

print(flower)

print("method 2: from pan")

for i in range(100, 1000):
    # 先转成字符串，方便提取位置上的数字
    s = str(i)
    if int(s[0]) ** 3 + int(s[1]) ** 3 + int(s[2]) **2 == i:
        print(i)
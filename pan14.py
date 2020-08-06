# 今天我们还是学习斐波那契数列。
# 有一个分数序列为 2/1，3/2，5/3，8/5，13/8，21/13……
# 请用Python3编程，求出这个数列的前20项之和。

L1 = [2, 3]
L2 = [1, 2]
sum = 2/1 + 3/2
for i in range(18):
    s = L1[-2] + L1[-1]
    k = L2[-2] + L2[-1]
    L1.append(s)
    L2.append(k)
    sum = sum + s/k

print(L1)
print(L2)
print(round(sum, 2))

# from pan
num = 2
den = 1
for i in range(1, 21):
    sum += num/den
    num, den = num + den, num
print(sum)
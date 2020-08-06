# 用Python3编程，求1!+2!+3!+……+n! 的和。

n = int(input())
m = 0
for i in range(1, n + 1):
    print("i = ", i)
    s = 1
    t = "1"
    for k in range(1, i + 1):
        s = s * k # s *= k
        t = t + "*" + str(k)
        print(t)
    m = m + s # m += s

print(m)

# from pan

n = int(input())

sum = 0
fac = 1
for i in range(1, n+1):
    fac *= i # fac = fac * i
    sum += fac
print(sum)

# 利用上一次的乘积
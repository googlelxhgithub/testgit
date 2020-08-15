# 请使用Python3语言编程，用三种办法计算1+2+3+4+...+99+100的和。

s = 0
for i in range(1, 101):
    s += i

print(s)

print("......")
def a(n):
    if n == 1:
        return 1
    else:
        return a(n-1) + n

print(a(100))

def b(n):
    if n == 100:
        return 100
    else:
        return b(n + 1) + n

print("...")
print(b(1))

print("method 4, 生成器表达式")
# sum = sum (x for x in range(101))
# print(sum)

c = sum (x for x in range(101))
print(c)
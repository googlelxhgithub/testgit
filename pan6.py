# 如何用程序来求任意两个数的最大公约数？

a = int(input("first: "))
b = int(input("second: "))

# 取最小的那个数
d = min(a, b)

for i in range(1, d+1):
    if a % i == 0 and b % i == 0:
        c = i
print(f"{a} and {b} number is {c}")

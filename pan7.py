# 最小公倍数是小学五年级的数学课程内容，小学生完成最小公倍数的学习后就可以升学到初中了。
# 如何用程序求出任意两个数的最小公倍数？

a = int(input("first: "))
b = int(input("second: "))


# 方法一：先算出最大公约数，在算最小公倍数

# 取最小的那个数
# d = min(a, b)

# for i in range(1, d+1):
#     if a % i == 0 and b % i == 0:
#         c = i
# print(f"{a} and {b} number1 is {c}")

# print(f"{a} and {b} number2 is {int(a*b/c)}")

# 方法二：遍历，找出能同时被两个数整除的数

c = max(a, b)


while True:
    if c%a == 0 and c%b == 0:
        break
    else:
        c = c + 1
print(f"{a} and {b} number2 is {int(c)}")    
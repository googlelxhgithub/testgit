# 素数（又名质数），即只能被数字 1 和⾃⾝整除、且⼤于 1 的⾃然数。
# 公元前 300多年，古希腊数学家欧⼏⾥得就证明了有多个素数的存在。
# 素数是“哥德巴赫猜想”等许多数学猜想的基础。
# 问题：如何列出 1 到 100 的素数数列，并计算出素数的个数？

# LST = []

# for i in range(1, 101):
#     Result = True
#     for s in range(1,i):
#         if (i % s == 0) and (s != 1):
#             Result = False
#             break
#     if Result:
#         LST.append(i)
        

# print(LST)
# print(len(LST))

# 知道x%y的使用

number = 0

for n in range(2, 101):
    for j in range(2, n): 
        if n%j == 0:
            break
    else:
        number += 1
        print(n, end = " ")

print(" ")
print("1-100之间的素数是%d个"%number)

# 这个写法很巧妙，但是可读性不强。用一个flag表示更好。比如叫is_prime_number，
# 每个外层循环开始设成True，内循环遇到任何一个可约的数就讲其设为False，并且break。
# 在外循环最后如果is_prime_number，number+=1。这样多写两行代码，复杂度一样，但是可读性强了很多
# (就是我的思路啊。。)

# for......else......的执行顺序为：
# 当迭代对象完成所有迭代后且此时的迭代对象为空时，如果存在else子句则执行else子句，
# 没有则继续执行后续代码；如果迭代对象因为某种原因（如带有break关键字）提前退出迭代，
# 则else子句不会被执行，程序将会直接跳过else子句继续执行后续代码

# 上面2为什么能打出来，因为range(2,2)，根本没有执行。。。
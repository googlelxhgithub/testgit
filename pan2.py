# 2020.8.1
# 学习了for...in..., if, !=

# 有四个数字为：1、2、3、4，他们能组成多少个互不相同、
# 且无重复数字的三位数？分别是多少？

# 定义一个列表，放入4个数字
L = [1, 2, 3, 4]
count = 0

for N1 in L:
    # print(N1)
    for N2 in L:
        if N2 != N1:
            for N3 in L:
                if N3 != N1 and N3 != N2:
                    # print(str(N1) + str(N2) + str(N3))
                    # print(N1,N2,N3)
                    print(f"{N1}{N2}{N3}")
                    # count = count + 1
                    count += 1

print(count)

# 直接用for .. in..., 不能写while ... in ..., 
# 相同就跳过。
# 数字组成，先转成字符。

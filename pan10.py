# 用Python3语言在编程猫海龟编辑器上，
# 如何将一个正整数分解质因数？
# 例如输入90，打印出90=2*3*3*5

# 只能被1和本身这两个不同的自然数整数的自然数叫质数，例如：2，3，5，7，11，......
# # 
# 思路：
# 输入一个数（字符），转换成整数；

# 让他被每一个质数除。
# # 
# n = input("int is: ")
# n = int(n)

# for i in range(2, n):
    # # 判断n是不是质因数
    # A = True
    # for k in range(2, n):
        # if n % k == 0:
            # A = False
            # break
    # # 如果是，就中断计算
    # if A:
        # # 把最后一个质因数打出来，并中断。
        # print(n)
        # break   
    # # 判断i是不是质因数False
    # for j in range(2, i):
        # if i % j == 0:
            # break
    # else:
        # print(f"test the number: {i}")
        # while n % i == 0:
            # print(i)
            # n = n//i
    
print("method 2:from pan:")

n = int(input("int is: "))
for k in range(2, n+1):
    while n != k:
        if n % k == 0:
            print(k)
            n = n/k
        else:
            break
print(int(n))
    
    




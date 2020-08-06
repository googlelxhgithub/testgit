# 请用Python3编程，利用递归方法求n!  (n为整数）

def fac(n):
    # 中断条件
    if n <= 1:
        print("n = ", n)
        print(1)
        return 1
    else:
        print("n = ", n)
        print(f"{n} * fac({n} - 1)")
        return n * fac(n-1) # 递归

n = int(input())
print("")

print(fac(n))
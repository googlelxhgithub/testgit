# 请使用Python3语言，
# 用四种方法将两个变量的值互换位置。
# 比如将a=3, b=4，互换后变成a=4, b=3。


a = 3
b = 4
print(a, b)
a, b = b, a

print(a, b)

a = 3
b = 4

c = a
a = b
b = c
print(a, b)

print(".....")
def f(a, b):
    list_1 = [a, b]
    list_2 = list_1[::-1]
    return list_2

print(f(3, 4))
# 2020.8.16

# 函数调用关系
# 测试文件f1.py, f2.py
# f1.py 定义函数
# f2.py调用f1.py

# 当使用from 模块名 import * 导入时p_a,只能导入指定函数
# _all__ = ['p_a']


def p_a(n):
    print(f"传递参数n，是{n}")

def p_b(n1, n2):
    print(f"传递参数n1, n2，是{n1}、{n2}")

# 内部调用
def p_c():
    p_a(100)

#函数内定义函数
def p_d():
    def p_d_1():
        print("it's ok?")
    p_d_1()

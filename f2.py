# 2020.8.16

# 函数调用关系
# 测试文件f1.py, f2.py

# 写法1：
# 导入所有函数

# import f1

# f1.p_a(3)
# f1.p_b(2, 3)

# 报错
# p_a(3) 

# 写法2：
# 导入特定的函数
#  from f1 import p_a
# p_a(3)

# 写法3：
# from f1 import *
# p_a(3)

# p_b(4, 5)

# p_c()

# p_d()

# 写法4：
# import f1 as abc

# abc.p_a(3)

# 写法4
from f1 import p_a as efg
efg(3)
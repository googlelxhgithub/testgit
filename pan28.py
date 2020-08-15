# 2020.8.9
# 请使用Python3语言编程，求在一个包含9个数字的数列中产生一个随机的、包含3个数字的新数列。
# 需要了解random

import random
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = random.choices(list_1, k = 3)
print(a)
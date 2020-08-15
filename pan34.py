# 俗话说：“四年一闰，百年不闰，四百年再闰”。
# 请使用Python3编程，输入一个年份，判断这一年是否是闰年。

y = int(input())

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print(f"{y}是闰年。")
else:
    print(f"{y}不是闰年。")


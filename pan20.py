
# 请用Python3编程判断某一个数是不是回文数。
# 例如12321就是一个回文数，
# 即这个数的个位与万位相同，十位与千位相同。

s = input()
# s1 = s[::-1]
# if int(s) == int(s1):
if s == s[::-1]
    print("it is ok.")
else:
    print("it is not.")
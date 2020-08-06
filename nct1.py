# 输入5个数，求平均数，结果为四舍五入后的整数。


score = input().split(" ")
t = 0
for s in score:
    t += int(s)

print(int(round(t/5, 0)))

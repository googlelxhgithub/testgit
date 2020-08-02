# 用Python3语言在编程猫的海龟编辑器上，
# 输入任意一个字符串，
# 如何才能得到空格、数字、字符和“其他”的个数？

# 学会使用isdigital, isspace, isalpha

# 输入任意字符串
s = input("plean input any strings: ")
l = len(s)
i = 0
sp = 0
nu = 0
al = 0
ot = 0
while i < l:
    print(s[i])
    # if s[i] == " ":
    if s[i].isspace():
        sp = sp + 1
    elif s[i].isdigit():
    # elif isinstance(s[i], int):
        nu = nu + 1
    elif s[i].isalpha():
    # elif isinstance(s[i], str):
        al = al + 1
    else:
        ot = ot + 1
    i = i + 1

print(f"space is {sp}, number is {nu}, alpha is {al}, ot is {ot}.")

# 方法二：from pan
# 使用字典，使用isdigital, isspace, isalpha

s = input("method2, string = ")
dit = {"sp":0, "di":0, "al":0, "ot":0}

# 只要这个字符在这个字符串中
for i in s:
    if i.isspace() == True:
        dit["sp"] += 1
    elif i.isdigit() == True:
        dit["di"] +=1
    elif i.isalpha() == True:
        dit["al"] += 1
    else:
        dit["ot"] += 1

print("method 2: ")
# print(f"space is {dit["sp"]}, number is {dit["di"]}, alpha is {dit["al"]}, ot is {dit["ot"]}.")
# 把字典打印出来：
print(dit)

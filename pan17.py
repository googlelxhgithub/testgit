# 请用Python3编程，利用递归函数调用的方式，
# 将所输入的5个字符，以相反顺序打印出来。

def rev(str, l):
    if l == 0:
        return
    else:
        print(str[l - 1], end = "")
        
        rev(str, l-1) # l -1 其实已经赋值给函数rev了。
    
str = input("string is：")

rev(str, len(str))
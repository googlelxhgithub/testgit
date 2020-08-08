# 使用Python3编程，
# 通过星期几的英语单词的第一个字母来判断是星期几，
# 如果第一个字母一样，则继续判断第二个字母。

# Monday, Tuesday, Wednesday, Thursday, Friday,Saterday, Sunday

week = { 
        "M" : "Monday", 
        "T" : {"U" : "Tuesday", "H" : "Thursday"},
        "W" : "Wednedsay",
        "F" : "Friday",
        "S" : {"A" : "Saterday", "U" : "Sunday"}
        }

i_1 = input("please input the first: ").upper()
if i_1 == "T" or i_1 == "S":
    i_2 = input("please input the second: ").upper()
    print(week[i_1][i_2])
else:
    print(week[i_1])


# 构造一个字典
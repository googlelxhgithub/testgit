# “倒计时”在我们日常生活中随处可见，
# 比如：交通标志、开工仪式、庆祝活动、 火箭升空。
# 但最戏剧化的还是电影 007 中定时炸弹的倒计时，还有《三体》中的倒计时信号。
# 今天的问题是：输入一个目标时间(包括年、月、日、时、分、秒)，
# 如何写出从当前时间开始到目标时间的倒计时?

from datetime import datetime 
import os
import time

DDay = input("目标日期(格式：YY/MM/DD HH:MM:SS) ")
# 把输入的日期打印出来，此时是字符形式。
print(DDay)
# 把字符形式转化为日期格式
DDay = datetime.strptime(DDay, "%Y/%m/%d %H:%M:%S")

while True:
    os.system('cls')
    NDay = datetime.now()

    # print(DDay, NDay)

    D = DDay - NDay

    DD = D.days
    secs = D.seconds
    HH = secs // 3600
    secs = secs % 3600
    MM = secs // 60
    secs = secs % 60
    print(f"{DD}天{HH}时{MM}分{secs}秒")
    time.sleep(1)



# cday = datetime.strptime("2017-8-1 18:20:20", "%Y-%m-%d %H:%M:%S")
# print(cday)

# print(cday.day)



# 今天跟朋友们一起学习“企业根据利润提成发奖金”的问题。
# 当利润(I)低于或等于10万元时，奖金可提10%；
# 当利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；
# 当20万到40万之间时，高于20万元的部分，可提成5%；
# 当40万到60万之间时高于40万元的部分，可提成3%；
# 当60万到100万之间时，高于60万元的部分，可提成1.5%；
# 当高于100万元时，超过100万元的部分按1%提成。
# 问题是求应发放奖金总数是多少？我稍后会在下一条公布答案。

# 输入利润，并赋值给一个变量

lirun = input("please tell me your profit: ")
# lirun = float(lirun)
lirun = int(lirun)

if lirun <= 10:
    money = lirun * 0.1
elif lirun > 10 and lirun <= 20:
    money = 10 * 0.1 + (lirun -10) * 0.075
elif lirun > 20 and lirun <= 40:
    money = 10 * 0.1 + (20 - 10) * .0075 + (lirun - 20) * 0.05
elif lirun > 40 and lirun <= 60:
    money = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (lirun - 40) * 0.03
elif lirun > 60 and lirun <= 100:
    money = 10 * .1 + 10 * .075 + 20 * 0.05 + 20 * 0.03 + (lirun - 60) * 0.015
elif lirun > 100:
    money = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (lirun - 100) * 0.01

print("this is your money: ", money)
    
# 倒过来写省点事情。。。
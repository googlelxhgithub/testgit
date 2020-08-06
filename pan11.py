# 两个乒乓球队进行单打比赛，每队各有三人。
# 其中甲队是a、b、c三人，乙队是x、y、z三人，
# 已根据抽签结果确定了比赛的名单，但没有公开，
# 有人向队员打听对战的名单。
# a 说：不和x比赛。
# c说：不和x、z比赛。
# 请在Python3运用集合的知识点进行编程，
# 算出三组赛手的名单。

# L1 = ["a", "b", "c"]
# # if "a" in L1:
    # # print("ok")
# L2 = ["x", "y", "z"]
# L3 = []

# for d in L1:
    # for e in L2:
        # print(e)
        # # 选过了，就不选了。
        # # if e in L3:
            # print("ok")
            # # pass # 就是不执行后续的if内的语句（if...elif..）
        # # a说，不和x比赛
        # elif d == L1[0] and e == L2[0]:
            # pass
        # elif d == L1[2] and e == L2 [0]:
            # pass
        # elif d == L1[2] and e == L2 [2]:
            # pass
        # # elif e in L3:
            # # pass
        # else:
            # print(d, "and", e)
            # L3.append(e)
            # # 选好了一对，进入下一对的选择
            # break
            
# print(L3)

# 先把所有组合找出来，再把不满足条件的去掉

# L1 = ["a", "b", "c"]
# L2 = ["x", "y", "z"]
# L3 = []
# i = 0

# for d in L1:
    # # i += 1
    # # print("组合：", i)
    # for e in L2:
        # # if e in L3:
            # # pass
        # # else:
            # # L3.append(e)
            # # print(d, e)
            # # break
        # L3.append([d,e])

# for s1 in L3:
    # for s2 in L3:
        # for s3 in L3:
            # if s1[0] == s2[0]  == s3[0]:
                # pass
            # elif s1[1] == s2[1] == s3[1]:
                # pass
            # else:
                # print(s1, s2, s3)

# method from pan
# set还可以相减

# 定义set
b = {"x", "y", "z"}
a = {"x", "y", "z"}
c = {"x", "y", "z"}
c = c - {"x", "z"}
a = a - {"x"}

for i in a:
    for j in b:
        for k in c:
            if len(set([i, j, k])) == 3:
                print(f"a:{i}, b:{j}, c:{k}")


# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
# set 集合
# 集合（set）是一个无序的不重复元素序列。
# 
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。 
# 集合可以运算
# a - b 只有a包含
# a | b 合并
# a & b 都包含
# a ^ b 不同时包含


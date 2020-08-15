# 已知一个已经排好序的数组，现在输入一个数，用Python3语言按原来的规律将它插入到数组中。

list_2 = [3, 5, 7, 9]
list_1 = [9, 7, 5, 3]

s_1 = int(input())

# 如果时从小到打：
# if list_1[-1] > list_1[-2]:
#     for i in range(len(list_1)):
#         if s_1 > list_1[-1-i] and i == 0:
#             list_1.append(s_1)
#             break
#         elif s_1 > list_1[-1-i]:
#             list_1.insert(-i, s_1)
#             break
#     else:
#         list_1.insert(-1-i, s_1)

# print(list_1)

if list_1[-1] > list_1[-2]: # 如果时升序
    for i in range(len(list_1)):
        if s_1 < list_1[i]:
            list_1.insert(i, s_1)
            break
    else: # for循环完以后，都不满足，则执行。。
        list_1.append(s_1)
else: # 如果是降序
    for i in range(len(list_1)):
        if s_1 > list_1[i]:
            list_1.insert(i, s_1)
            break
    else:
        list_1.append(s_1)

print(list_1)

# from pan
# 考虑不完整，指考虑了升序，另外只考虑了中间插入的情况。。

print("method from pan: ")
list_1 = [1, 2, 3, 4, 5, 6, 7]
num_1 = int(input())

for i, v in enumerate(list_1):
    if num_1 < v:
        list_1.insert(i, num_1)
        break
print(list_1)
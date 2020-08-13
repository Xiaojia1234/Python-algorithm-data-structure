#使用动态规划求解0-1背包问题
#老三
info = [
    [3, 8],
    [2, 5],
    [5, 12]
]
total = 5
#老三初始化
pre_max = [0]
for i in range(1, info[-1][0]):
    pre_max.append(0)
for i in range(info[-1][0], total+1):
    pre_max.append(info[-1][1])

# #老二
# new_pre_max = [0]
# for i in range(1, total+1):
#     value_list = []
#     for j in range(0, i + 1):
#         #j代表留给自己
#         if j >= info[1][0]:
#             value_list.append(info[1][1]+pre_max[i-j])
#         else:
#             value_list.append(pre_max[i-j])
#     new_pre_max.append(max(value_list))
#
# #老大
# new_pre_max2 = [0]
# for i in range(total, total+1):
#     value_list = []
#     for j in range(0, total+1):
#         #j代表留给自己
#         if j >= info[0][0]:
#             value_list.append(info[0][1]+new_pre_max[i-j])
#         else:
#             value_list.append(new_pre_max[i-j])
#     new_pre_max2.append(max(value_list))


# 自底向上
for k in range(len(info)-1, -1, -1):
    # pre_max存储每一层剩余空间对应得最大价值的list
    new_pre_max = [0]
    start = 1
    # if k == 0:
    #     start = total
    # total为总容量
    for i in range(start, total + 1):
        value_list = []
        # 判断拿到的容量与当前物品的容量的大小，以获取对应的最大价值
        if i >= info[k-1][0]:
            # 每一个组合的最大价值添加到新的pre_max里面
            value_list.append(info[k-1][1] + pre_max[i-info[k-1][0]  ])
        value_list.append(pre_max[i])
        new_pre_max.append(max(value_list))
    pre_max = new_pre_max
print(pre_max)


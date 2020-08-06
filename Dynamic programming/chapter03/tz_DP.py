'''
投资分配问题：
一共右60万元，如何分配给这四个人可以使利润最大？

利润表:
表示老大、老二、老三、老四分别在投资10~60万元时候（以十万元为间隔），可以得到的利润

'''
values = [
    [0,20,50,65,80,85,85],
    [0,20,40,50,55,60,65],
    [0,25,60,85,100,110,115],
    [0,25,40,50,60,65,70]
]
# # 分析过程：
# # 老三统计好各种情况
# pre_max = [0]
# for i in range(10, 61, 10):
#     # i代表老三拿到的投资总数
#     value_list = []
#     # j代表老四拿到的投资总数
#     for j in range(0, i+1, 10):
#         # print(i, j)
#         value_list.append(values[3][int(j/10)] + values[2][int((i-j)/10)])
#     pre_max.append(max(value_list))
#     # print(value_list)
# print(pre_max)
#
# # 老二统计好各种情况
# pre_max2 = [0]
# for i in range(10, 61, 10):
#     # i代表老三拿到的投资总数
#     value_list = []
#     # j代表老四拿到的投资总数
#     for j in range(0, i+1, 10):
#         # print(i, j)
#         value_list.append(pre_max[int(j/10)] + values[1][int((i-j)/10)])
#     pre_max2.append(max(value_list))
#     # print(value_list)
# print(pre_max2)
#
# # 老大统计好各种情况
# pre_max3 = []
# for i in range(60, 61, 10):
#     # i代表老三拿到的投资总数
#     value_list = []
#     # j代表老四拿到的投资总数
#     for j in range(0, i+1, 10):
#         # print(i, j)
#         value_list.append(pre_max2[int(j/10)] + values[0][int((i-j)/10)])
#     pre_max3.append(max(value_list))
#     # print(value_list)
# print(pre_max3)


# 整合版：
pre_max = values[3]
for k in range(len(values)-1,-1,-1):
    new_pre_max  = [0]
    for i in range(10, 61, 10):
        # i代表老三拿到的投资总数
        value_list = []
        # j代表老四拿到的投资总数
        for j in range(0, i + 1, 10):
            # print(i, j)
            value_list.append(pre_max[int(j / 10)] + values[k-1][int((i - j) / 10)])
        new_pre_max.append(max(value_list))
    pre_max = new_pre_max

print(pre_max)


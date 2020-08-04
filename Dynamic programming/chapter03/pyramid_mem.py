# 数字金字塔
'''
选择最优的路径使和最大
动态规划：求解最优的问题
'''


pyramid = [
    [13],
    [11,8],
    [12,7,26],
    [6,14,15,8],
    [12,17,13,24,11]
]


# 原版
# def search_max(depth,y):
#     if depth == 4:
#         return pyramid[depth][y]
#     else:
#         # 1.把垂直方向下方的值交给下一个人 得到最大值
#         left_max = search_max(depth+1,y)
#         # 2.把垂直方向右下方的值交给下一个人 得到最大值
#         # 1.任务可以下分；2.最优子结构，3.决策
#         right_max = search_max(depth + 1, y + 1)
#         return pyramid[depth][y] + max(left_max,right_max)

info = {}
# 化简版本
def search_max(depth,y):
    if depth == 4:
        return pyramid[depth][y]
    if "{}_{}".format(depth,y) in info:
        return info["{}_{}".format(depth,y)]
    else:
        max_value = pyramid[depth][y] + max(search_max(depth+1,y),search_max(depth + 1, y + 1))
        info["{}_{}".format(depth,y)] = max_value
        return max_value


# 练习 求最小路径
info2 = {}
def search_min(depth,y):
    if depth == 4:
        return pyramid[depth][y]
    if "{}_{}".format(depth,y) in info2:
        return info2["{}_{}".format(depth,y)]
    else:
        min_value = pyramid[depth][y] + min(search_min(depth+1,y),search_min(depth+1,y+1))
        info2["{}_{}".format(depth, y)] = min_value
        return min_value




if __name__ == "__main__":
    print(search_max(0,0))
    print(info)
    print(search_min(2,0))
    print(info2)
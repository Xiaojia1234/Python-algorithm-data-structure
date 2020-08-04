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
    [12,7,13,24,11]
]


max_value = 0
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


# 化简版本
def search_max(depth,y):
    if depth == 4:
        return pyramid[depth][y]
    else:
        return pyramid[depth][y] + max(search_max(depth+1,y),search_max(depth + 1, y + 1))



if __name__ == "__main__":
    print(search_max(3,0))
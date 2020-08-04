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
def search_max(depth,y):
    # 1.把垂直方向下方的值交给下一个人 得到最大值
    left_max = search_max(depth+1,y)
    # 2.把垂直方向右下方的值交给下一个人 得到最大值
    right_max = search_max(depth + 1, y + 1)
    return pyramid[depth][y] + max(left_max,right_max)




if __name__ == "__main__":
    search_max(1,0)
# 数字金字塔
'''
选择最优的路径使和最大

'''

pyramid = [
    [13],
    [11,8],
    [12,7,26],
    [6,14,15,8],
    [12,7,13,24,11]
]

datas = [13]
total_path = []
def search(depth,x,y):
    if depth == 5:
        # print(datas)
        total_path.append(datas[:])
    else:
        # 1.选择下方的值
        # 1.设置现场
        datas.append(pyramid[x+1][y])
        # 2.递归
        search(depth+1,x+1,y)
        # 3.恢复现场
        datas.pop()

        # 1.选择右下方的值
        # 1.设置现场
        datas.append(pyramid[x+1][y+1])
        # 2.递归
        search(depth + 1, x + 1, y+1)
        # 3.恢复现场
        datas.pop()

if __name__ == "__main__":
    search(1,0,0)
    max = 0
    max_pos = 0
    for index,data in enumerate(total_path):
        if sum(data) > max:
            max = sum(data)
            max_pos = index
    print(max_pos,sum(total_path[max_pos]),total_path[max_pos])
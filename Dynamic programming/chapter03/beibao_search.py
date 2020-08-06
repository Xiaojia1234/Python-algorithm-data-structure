'''
0-1背包问题：
徒步旅行者，可携带物品险种为a公斤，右n种物品可选择装入包中，
已知每种物品的重量及其使用价值，问此人如何选择携带的物品，使使用价值最大？
类似问题：
工厂下料问题、运输过程中的货物装载问题、人造卫星内物品装载问题
'''

# 1. 通过回溯法求解0-1背包问题

info = [
    [3,8],
    [2,5],
    [5,12]
]

selects = []
max_select = []
max_value = 0
def search(depth,rest):
    if depth == 3:
        print(selects)
        values = []
        for index,select in enumerate(selects):
            values.append(select*info[index][1])
        global max_value
        if sum(values) > max_value:
            max_value = sum(values)
            print(max_value)
            global max_select
            max_select = selects[:]
    else:
        # 1. 不放
        # 1.设置现场
        selects.append(0)
        # 2.递归
        search(depth+1,rest)
        # 3.恢复现场
        selects.pop()
        # 2. 放
        if rest >= info[depth][0]:
            # 1.设置现场
            selects.append(1)
            # 2.递归
            search(depth + 1, rest-info[depth][0])
            # 3.恢复现场
            selects.pop()


if __name__ == "__main__":
    search(0,5)
    print(max_select)



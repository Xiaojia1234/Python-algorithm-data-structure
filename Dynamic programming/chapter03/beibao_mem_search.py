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
mem = {}
def search(depth,rest):
    # 放还是不放，决策
    if "{}_{}".format(depth,rest) in mem:
        return mem["{}_{}".format(depth,rest)]
    if depth == 2:
        data = info[depth][1] if rest >= info[depth][0] else 0
    else:
        # 1.分任务
        values = []
        values.append(search(depth+1,rest))
        if rest >= info[depth][0]:
            values.append(search(depth+1,rest-info[depth][0]) + info[depth][1])
        # 2.选最大
        data = max(values)
    if "{}_{}".format(depth,rest) not in mem:
        mem["{}_{}".format(depth, rest)] = data
    return data

if __name__ == "__main__":
    print(search(0,5))
    print(mem)



'''
1,2,3的全排列
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1
3 1 2
# 所有
1. 先处理第一个  老大选择一个，剩余的交给老二
2. 老二，选择剩余里面的一个，剩余的再交给老三
3. 只有一个
'''

data_list = [1,2,3,4,5]
arranges = []
total = 0
def search(depth,datas):
    if depth == len(data_list)+1:
        # arranges.append(datas[0])
        print(arranges)
        # arranges.pop()
        global total
        total+=1
    else:
        for data in datas:
            #1. 设置现场
            arranges.append(data)
            #2. 递归
            next_datas = datas[:]
            next_datas.remove(data)
            search(depth+1,next_datas)
            #3. 恢复现场
            arranges.pop()

if __name__ == "__main__":
    search(1,data_list)
    print("有{}种排列方式".format(total))





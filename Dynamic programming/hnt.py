#1.大傻：只搬动一号盘
#2. 1.叫谁来做；1.从哪个柱子搬到哪个柱子，中间柱子是谁
#2. 2.搬动子集负责的柱子，3.叫谁把盘子从哪个柱子移动到哪个柱子，中间柱子

def move(index,start,mid,end):
    if index == 1:
        print("{}-->{}".format(start, end))
        return
    else:
        move(index-1,start,end,mid)
        print("{}-->{}".format(start,end))
        move(index-1,mid,start,end)


if __name__ == "__main__":
    move(5,"A","B","C")
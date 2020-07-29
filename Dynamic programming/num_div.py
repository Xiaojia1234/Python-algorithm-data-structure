'''
 数字拆分
num = 7 和为7的所有数字组合：
1+1+1+1+1+1+1
1+2+4
2+3+2
……
1. 老大拿到数字后，先尝试所有可能的取值，上一个人分给自己的值
2. 把上一个人分给自己的值拿到后，尝试所有的取值，再把剩下的分给下一个人

'''

num = 7

datas = []
total = 0
def search(rest):
    if rest <= 0:
        print(datas)
        global total
        total+=1
    else:
        for i in range(1,rest+1):
            #1.设置现场
            datas.append(i)
            #2.递归
            search(rest-i)
            datas.pop()

if __name__ == "__main__":
    search(num)
    print("共有{}种数字组合".format(total))
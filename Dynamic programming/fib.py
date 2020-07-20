# 斐波那契额数列

# 什么地方调用递归本身
# 什么时候终止递归
# 1 1 2 3 5 8 13 21 34 55 89
def fib_test(k):
    #求解第k个数的值
    if k in [1,2]:
        return 1
    return fib_test(k-1) + fib_test(k-2)



if __name__=="__main__":
    print(fib_test(4))
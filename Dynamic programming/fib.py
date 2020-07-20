# 斐波那契额数列



# 递归实现
# 什么地方调用递归本身
# 什么时候终止递归
# 1 1 2 3 5 8 13 21 34 55 89

from collections import defaultdict
total = defaultdict(int)
def fib_test(k):
    #求解第k个数的值
    if k in [1,2]:
        return 1
    global total
    total[k] += 1
    # if k not in total:
    #     total[k] = 1
    # else:
    #     total[k] += 1
    return fib_test(k-1) + fib_test(k-2)




# 不使用递归方法
def fib_test2(k):
    assert k > 0, "k 必须大于0"
    k_1 = 1
    k_2 = 1
    if k in [1,2]:
        return 1
    for i in range(3,k+1):
        i_value = k_1 + k_2
        temp = k_1
        k_1 = i_value
        k_2 = temp
    return k_1




if __name__=="__main__":
    print(fib_test(7))
    print(fib_test2(8))
    from datetime import datetime
    start_time = datetime.now()
    print(fib_test(36))
    print("递归耗时：{}".format((datetime.now()-start_time).total_seconds())) # kite
    print(total)

    start_time = datetime.now()
    print(fib_test2(100))
    print("循环耗时：{}".format((datetime.now() - start_time).total_seconds()))  # kite
    # print(total)
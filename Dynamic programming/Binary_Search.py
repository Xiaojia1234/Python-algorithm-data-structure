data = [1, 7, 17, 18, 27, 29, 30, 35, 39, 41, 63, 63, 66, 67, 78, 82, 91, 92]

# 二分查找：折半查找（针对有序数组）

def search(data_list,target):
    left = 0
    right = len(data_list)-1
    target_pos = -1
    while left <= right:
        #1. 找到left 和 right 的中间值
        mid = int((left + right)/2)
        # 2.判断中间值和目标值的大小
        if data_list[mid] == target:
            target_pos = mid
            break
        elif data_list[mid]<target:
            # 如果中间值小于目标值，则在右侧继续二分查找
            left = mid + 1
        else:
            # 如果中间值大于目标值，则在左侧继续查找
            right = mid -1
    return target_pos



def search2(left, right, data_list, target):
    mid = int((left + right) / 2)
    if data_list[mid] == target:
        return mid
    elif data_list[mid] < target:
        # 如果中间值小于目标值，则继续在右侧二分查找
        return search2(mid+1, right, data_list, target)
    else:
        # 如果中间值大于目标值，则在左侧继续查找
        return search2(left, mid-1, data_list, target)


if __name__ == "__main__":
    # pos = search(data,100)
    pos = search2(0,len(data)-1,data, 29)
    if pos >= 0 :
        print("查询到数据，所在位置：{}".format(pos))
    else:
        print("目标值不在列表中")



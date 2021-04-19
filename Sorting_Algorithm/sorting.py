'''
冒泡排序：

复杂度：在该排序算法中，要遍历n-1轮，每一轮都要比较数组中的元素，所以时间复杂度是O(n2)
稳定性：比较的过程中相同的元素并不会发生交换，所以冒泡排序是一种稳定的排序算法。

相邻的两个元素进行比较，然后把较大的元素放到后面（正向排序），在一轮比较完后最大的元素就放在了最后一个位置，
因为这一点像鱼儿在水中吐的气泡在上升的过程中不断变大，所以得名冒泡排序。在该排序算法中，要遍历n-1轮，
每一轮都要比较数组中的元素，所以时间复杂度是O(n2)
'''

alist = [1,5,2,76,3,2,7,8,4,23,78,32,65]

def bubble_sort(alist):
    length = len(alist)
    for i in range(length - 1):
        # i表示比较多少轮
        for j in range(length - i - 1):
            # j表示每轮比较的元素的范围，因为每比较一轮就会排序好一个元素的位置，
            # 所以在下一轮比较的时候就少比较了一个元素，所以要减去i
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
            # print(i,j,alist)
    return alist

# print("bubble_sort:",bubble_sort(alist))


def my_bubble_sort(alist):
    length = len(alist)
    for i in range(length - 1):
        for j in range(length-1-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
    return alist

# print('my_bubble_sort:',my_bubble_sort(alist))


'''
选择排序：
复杂度：每遍历一次排好一个元素，而每一次都会比较所有的元素，所以时间复杂度为O(n2)
稳定性：因为在交换的过程中，相同的元素位置可能发生变化，所以选择排序是不稳定的

第一轮的时候，所有的元素都和第一个元素进行比较，如果比第一个元素大，就和第一个元素进行交换，
在这轮比较完后，就找到了最小的元素；第二轮的时候所有的元素都和第二个元素进行比较找出第二个位置的元素，以此类推。
'''

def selection_sort(alist):
    length = len(alist)
    for i in range(length - 1,0,-1):
        for j in range(i):
            if alist[j] > alist[i]:
                alist[j],alist[i] = alist[i],alist[j]
            print(i,j,alist)
    return alist

print('selection_sort:',selection_sort(alist))


































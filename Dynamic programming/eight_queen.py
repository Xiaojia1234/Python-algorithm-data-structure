'''八皇后问题
8*8的棋盘上，每一个被放置的皇后都可以任意吃掉米字型路径上的东西，
要放置八个皇后，使八个皇后可以在期盼上共存，有多少种放法？
'''

'''
第一：分别尝试所有的位置
第二：分别尝试所有的问题- 这个不能和已有的皇后冲突 智能放第二排
      将任务下放
第三：分别尝试所有的问题- 这个不能和已有的皇后冲突 智能放第三排
      将任务下放

什么时候结束？

'''

board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]
total = 0

def can_place(x,y):
    # 判断x y坐标能否放皇后
    # 1. 判断x 行是否有皇后
    for i in range(0,y):
        if board[x][i] ==1:
            return False
    # 2. 判断y列是否有皇后
    for i in range(0,x):
        if board[i][y] == 1:
            return False
    # 3. 判断“/”方向是否有皇后 x+y为固定值
    for i in range(0,x):
        if x+y-i <= 7 and board[i][x+y-i] == 1:
            return False
    # 4. 判断：“\”方向是否有皇后
    for index,i in enumerate(range(x-1,-1,-1)):
        s_y = y - (index+1)
        if s_y >= 0:
            if board[i][s_y] == 1:
                return False
    return True

def print_board():
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                print("□ ",end=" ")
            else:
                print("■ ",end=" ")
        print("")

def put_queen(step):
    if step == 8:
        print_board()
        global total
        total += 1
        print("----------------------")
    else:
        for i in range(8):
            # 判断该位置是否能放置当前皇后
            if can_place(step,i):
                # 1. 设置现场
                board[step][i] = 1
                # 2. 开始递归
                put_queen(step+1)
                # 3. 恢复现场
                board[step][i] = 0

if __name__ == "__main__":
    # print_board()
    put_queen(0)
    print("总共有{}种方法".format(total))





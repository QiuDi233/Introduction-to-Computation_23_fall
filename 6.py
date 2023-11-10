# 6:海底垃圾检测
# 查看提交统计提问
# 总时间限制: 2000ms 内存限制: 131072kB
# 描述
# 人类丢弃到海底的垃圾会危害生物资源和人类健康，破坏海水质量。我们想设计一种海底垃圾检测装置，该装置可以检测给定坐标的海底地块以及它周围八个相邻的海底地块组成的九宫格内已经被丢弃的垃圾总量。

# 已知每次丢弃的垃圾沉入到海底的地块坐标和垃圾量。

# 请你帮忙模拟这个海底垃圾检测装置，输入任意的海底地块坐标，输出该装置的检测结果。

# 输入
# 第一行有一个整数n，n<=200000，表示所有垃圾丢弃记录。
# 接下来n行每行三个整数，第i行的三个整数分别表示第i个垃圾丢弃记录所在海底地块的横坐标、纵坐标和丢弃的垃圾量，记为tx_i, ty_i和tw_i。
# 接下来一个整数m。
# 接下来m行每行两个整数，第i行的两个整数表示垃圾检测装置的坐标，记为qx_i和qy_i。

# 1 <= tx_i, qx_i, ty_i, qy_i <= 1000000000;
# 1 <= tw_i <= 9
# 输出
# m行，每行一个整数，表示海底垃圾的检测结果。
# 样例输入
# 5
# 2 2 2
# 2 3 1
# 2 4 1
# 3 1 3
# 2 2 4
# 3
# 3 1
# 4 1
# 3 3
# 样例输出
# 9
# 3
# 8
# 提示
# 每个海底地块可能会被多次投放垃圾。
# 坐标范围可能很大，请使用字典完成本题。

def calc_garbage_sum(grid, x, y):
    garbage_sum = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) in grid:
                garbage_sum += grid[(i, j)]
    return garbage_sum
n = int(input())
grid = {}
for _ in range(n):
    tx, ty, tw = map(int, input().split())
    if (tx, ty) not in grid:
        grid[(tx, ty)] = 0
    grid[(tx, ty)] += tw
m = int(input())
queries = []
for _ in range(m):
    qx, qy = map(int, input().split())
    queries.append((qx, qy))
for qx, qy in queries:
    garbage_sum = calc_garbage_sum(grid, qx, qy)
    print(garbage_sum)
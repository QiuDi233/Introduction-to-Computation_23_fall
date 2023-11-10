# 4:找因子
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 给定正整数n和m，在[1,n]区间内取出两个不同的数，使得它们的和是m的因子，问有多少种取法？

# 输入
# 整数n和m，以空格分开。n∈[1,50]，m∈[10，100]
# 输出
# 输出每一种取法，按第一个数从小到大排序，如果第一个数相同则按第二个数从小到大排序。
# 如果不存在取法，那么输出"none"
# 样例输入
# 输入样例1：
# 26 16

# 输入样例2：
# 3 86
# 样例输出
# 输出样例1：
# 1 3
# 1 7
# 1 15
# 2 6
# 2 14
# 3 5
# 3 13
# 4 12
# 5 11
# 6 10
# 7 9

# 输出样例2：
# none
# 提示
# 输入部分代码提示：
# n, m = input().split(' ')
# n, m = int(n), int(m)


n, m = map(int, input().split())
pairs = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if m % (i + j) == 0:
            pairs.append((i, j))
if len(pairs) == 0:
    print("none")
else:
    pairs.sort()
    for pair in pairs:
        print(pair[0], pair[1])
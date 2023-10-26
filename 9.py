# 描述
# 将正整数n 表示成一系列正整数之和，n=n1+n2+…+nk, 其中n1>=n2>=…>=nk>=1 ，k>=1 。
# 正整数n 的这种表示称为正整数n 的划分。正整数n 的不同的划分个数称为正整数n 的划分数

# 输入
# 一个整数N(0 < N <= 30)。
# 输出
# 输出N的划分数。
# 样例输入
# 5
# 样例输出
# 7
# 提示
# 5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1

def count_partitions(N):
    # 创建一个二维数组 dp，dp[i][j] 表示将正整数 j 表示为不超过 i 的正整数之和的划分数
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # 初始化边界条件
    for i in range(N + 1):
        dp[i][0] = 1

    # 填充 dp 数组
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if j >= i:
                dp[i][j] = dp[i - 1][j] + dp[i][j - i]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[N][N]

# 读取输入并计算划分数
N = int(input())
result = count_partitions(N)
print(result)

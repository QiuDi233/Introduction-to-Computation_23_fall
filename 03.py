# 03:扫雷游戏

# 总时间限制: 1000ms 内存限制: 65535kB
# 描述
# 扫雷游戏是一款十分经典的单机小游戏。在 n 行 m 列的雷区中有一些格子含有地雷（称之为地雷格），其他格子不含地雷（称之为非地雷格）。玩家翻开一个非地雷格时，该格将会出现一个数字——提示周围格子中有多少个是地雷格。游戏的目标是在不翻出任何地雷格的条件下，找出所有的非地雷格。

# 现在给出 n 行 m 列的雷区中的地雷分布，要求计算出每个非地雷格周围的地雷格数。

# 注：一个格子的周围格子包括其上、下、左、右、左上、右上、左下、右下八个方向上与之直接相邻的格子。

# 输入
# 第一行是用一个空格隔开的两个整数 n 和 m，分别表示雷区的行数和列数。

# 接下来 n 行，每行 m 个字符，描述了雷区中的地雷分布情况。字符 * 表示相应格子是地雷格，字符 ？表示相应格子是非地雷格。相邻字符之间无分隔符。
# 输出
# 输出文件包含 n 行，每行 m 个字符，描述整个雷区。用 * 表示地雷格，用周围的地雷个数表示非地雷格。相邻字符之间无分隔符。
# 样例输入
# 3 3
# *??
# ???
# ?*?
# 样例输出
# *10
# 221
# 1*1
# 来源
# NOIP2015 普及组 T2

def count_mines(board, i, j, n, m):
    if board[i][j] == '*':
        return '*'

    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == '*':
                count += 1

    return str(count)

def minesweeper(n, m, board):
    result = [['' for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = count_mines(board, i, j, n, m)

    return result

n, m = map(int, input().split())
board = [input() for _ in range(n)]

result_board = minesweeper(n, m, board)

for row in result_board:
    print(''.join(row))
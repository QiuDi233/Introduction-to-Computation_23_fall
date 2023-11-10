# 1:统计成绩
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 现在一位老师手中有若干名学生的语数英三科成绩的成绩单，求每位学生的总成绩、平均成绩，并输出。

# 输入
# 一个整数 n 表示学生数量。接下来有 n 行，表示成绩。每行对应一个学生，包含 3 个数，每个数用空格隔开，分别对应语数英三科的成绩。
# 输出
# 输出 n 行，每行两个数，分别表示总成绩和平均成绩，均保留1位小数。（格式：这两个数用一个空格隔开）
# 样例输入
# # 样例 1
# 2
# 95 91.5 89
# 83.5 89 98
# 样例输出
# # 样例 1
# 275.5 91.8
# 270.5 90.2
# 提示
# # 获取输入代码
# grade = []
# n = int(input())
# for i in range(n):
#     grade.append([float(g) for g in input().split(" ")])
# grade 是一个储存成绩的二维列表，每个学生的成绩是一个列表

grade = []
n = int(input())
for i in range(n):
    grade.append([float(g) for g in input().split(" ")])
    for j in range(len(grade)):
        total=sum(grade[j])
        average=round((total/3),1)
    print(total,average)
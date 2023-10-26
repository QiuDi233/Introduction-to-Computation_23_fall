# 描述
# 在一个有180人的大班级中，存在两个人生日相同的概率非常大，现给出每个学生的学号，出生月日。试找出所有生日相同的学生。
# 输入
# 第一行为整数n，表示有n个学生，n<100。
# 此后每行包含一个字符串和两个整数，分别表示学生的学号（字符串长度小于10）和出生月(1<=m<=12)日(1<=d<=31)。
# 学号、月、日之间用一个空格分隔。
# 输出
# 对每组生日相同的学生，输出一行，
# 其中前两个数字表示月和日，后面跟着所有在当天出生的学生的学号，数字、学号之间都用一个空格分隔。
# 对所有的输出，要求按日期从前到后的顺序输出。
# 对生日相同的学号，按输入的顺序输出。
# 样例输入
# 5
# 00508192 3 2
# 00508153 4 5
# 00508172 3 2
# 00508023 4 5
# 00509122 4 5

# 样例输出
# 3 2 00508192 00508172
# 4 5 00508153 00508023 00509122

# 读取输入数据
n = int(input())
students = {}
for i in range(n):
    info = input().split()
    month, day = map(int, info[1:])
    if (month, day) in students:
        students[(month, day)].append(info[0])
    else:
        students[(month, day)] = [info[0]]

for key in sorted(students.keys()):
    if len(students[key]) > 1:
        print(key[0], key[1], ' '.join(sorted(students[key])))
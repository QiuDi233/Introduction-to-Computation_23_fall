# 0:学生信息管理
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 编写一个Python程序，使用一个字典来记录学生的学号和姓名。程序支持学生字典的增加和查询操作，输入的形式如下：

# a 211001 Liuli 表示向字典中添加一个学号为"211001"的学生，其名字为Liuli，如果字典中已经存在这个同学，这个操作就表示修改同学的姓名。

# q 211001 表示查询学生学号为"211001"的输出，如果字典里有这个学号，就输出ta的姓名，否则输出Not found!

# e表示输入结束，程序退出。

# 输入
# 任意行输入，最后一行是e，表示输入结束。
# 如果输入的首字母是a，则表示向字典中添加一个学生，格式为a 学号 姓名。
# 如果输入的首字母是q，则表示向字典中查询一个学生的姓名，格式为q 学号。
# 输出
# 对于每一行q开头的输入，输出此时字典中这个学生的姓名，如果该学生不存在于字典，那么输出Not found!
# 样例输入
# a 211001 Liuli
# a 210109 Guoming
# q 211001
# a 211001 Xueqiang
# q 210620
# q 211001
# e
# 样例输出
# Liuli
# Not found!
# Xueqiang

id_dict = {}
while True:
    id = input().split(' ')
    if id[0] == 'a':
        id_dict[id[1]] = id[2]
    elif id[0] == 'q':
        name = id_dict.get(id[1])
        if name:
            print(name)
        else:
            print('Not found!')
    elif id[0] == 'e':
        break

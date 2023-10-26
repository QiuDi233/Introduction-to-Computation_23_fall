# 描述
# 输入n行，每行不超过100个无符号整数，无符号数不超过4位。请输出最大整数以及最大整数所在的行号（行号从1开始）。如果该数据在多个行中出现，则按从小到大输出相应行号，行号之间以一个逗号分开。

# 输入
# 一行输入一个正整数n（n <= 30）。
# 之后的n行，每行包含不超过100个无符号整数，整数之间以一个逗号分开。
# 输出
# 第一行：最大整数；
# 第二行：最大整数所在的行编号，逗号间隔。
# 样例输入
# 6
# 1,3,5,23,6,8,14
# 20,22,13,4,16
# 23,12,17,22
# 2,6,10,9,3,6
# 22,21,20,8,10
# 22,1,23,6,8,19,23
# 样例输出
# 23
# 1,3,6

n=int(input())
lst=[]
lst1=[]
lst2=[]
for i in range(n):
    lst3=list(map(int,input().split(",")))
    lst=lst+lst3
    lst1.append(lst3)
num=max(lst)
print(num)
for i in range(n):
    if num in lst1[i]:
        lst2.append(i+1)
for i in range(len(lst2)):
    if i!=len(lst2)-1:
        print(lst2[i],end=",")
    else:
        print(lst2[i])
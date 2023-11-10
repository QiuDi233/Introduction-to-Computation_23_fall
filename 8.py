# 8:商品评分
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65535kB
# 描述
# 购物网站上有许多商品。每个商品都会得到若干用户评分（为1-10的正整数），取这些评分的平均数作为商品总评分。 给出各个商品的名称及其对应的若干用户评分，请按照商品总评分从高到低的顺序输出商品名称；如果两个商品总评分相同，则用户评分数量多的商品排在前面。

# 题目保证商品名称各不相同，且不会出现两个总评分与用户评分数量完全相同的商品。 本题目有多组输入数据。



# 输入
# 第一行一个整数n，表示数据组数；
# 接下来n组数据，每组数据中：
# 第一行一个整数m，表示该组数据中商品个数；
# 接下来m行，每行由一个字符串s（只含大小写字母）和若干个正整数（至多50个）组成，分别表示商品名称和用户评分。
# 输出
# 对于每组数据，按题目要求的排序结果，每行输出一个商品名称。
# 样例输入
# 2
# 3
# Apple 10 8
# Banana 9 9 9
# Peach 10 9
# 3
# Apple 10 8
# Banana 9 
# Peach 9 8
# 样例输出
# Peach
# Banana
# Apple
# Apple
# Banana
# Peach

n=int(input())
for i in range(n):
    m=int(input())
    dict1={}
    for k in range(m):
        lst=list(map(str,input().split()))
        name=lst[0]
        lst=lst[1:]
        lens=len(lst)
        num=0
        for j in range(lens):
            num+=int(lst[j])
        num/=lens
        dict1[name]=(lens,num)
    dict1=dict(sorted(dict1.items(),key=lambda x:(-x[1][1],-x[1][0])))
    lst1=list(dict1.keys())
    for k in range(len(lst1)):
        print(lst1[k])
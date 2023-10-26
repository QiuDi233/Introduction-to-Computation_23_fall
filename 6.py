# 描述
# 有n盏灯，编号为1~n。第1个人把所有灯打开，第2个人按下所有编号为2的倍数的开关（这些灯将被关掉），第3个人按下所有编号为3的倍数的开关（其中关掉的灯将被打开，开着的灯将被关闭），依此类推。一共有k个人，问最后有哪些灯开着？
# 输入
# n和k（k<=n<=1000）
# 输出
# 开着的灯编号。
# 样例输入
# 7 3
# 样例输出
# 1 5 6 7

n,k=map(int, input().split())
on = []
for i in range(1,n+1):
    num = 0
    for m in range(1,k+1):
        if i%m==0:
            num+=1
    if num%2 ==1:
        on.append(i)
str1=str(on[0])
for x in range(1,len(on)):
    str1 = str1 +" "+str(on[x])
print(str1)
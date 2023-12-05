n=int(input())
shuju=[]
huase=["d","c","h","s"]
paimian=["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
for i in range(0,n):
    r,p=input().split()
    p=str(p)
    for x in range(0,len(paimian)):
        if len(p)==2:
            if p[1]==paimian[x]:
                a=x
        else:
            if str(p[1])+str(p[2])==paimian[x]:
                a=x
    for y in range(0,len(huase)):
        if p[0]==huase[y]:
            b=y
    shuju.append((a,b,r))
shuju.sort()
shuju.reverse()
for j in range(0,n):
    print(shuju[j][2],end=" ")
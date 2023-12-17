import math
def f(a,b,x,y):
    l=math.sqrt((a-x)**2+(b-y)**2)
    return l
n=int(input())
l=[]
l1=[]
while n>0:
    a,b=map(float,input().split())
    l.append([a,b])
    n-=1
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        le=f(float(l[i][0]),float(l[i][1]),float(l[j][0]),float(l[j][1]))
        l1.append(float(le))
print("%.2f"%max(l1))
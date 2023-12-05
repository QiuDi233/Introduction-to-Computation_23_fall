n,m = map(int, input().split() )
names=[]
specialfirstname=[]
frequency={}
for i in range(n):
    names.append(input())
for i in range(m):
    specialfirstname.append((input()))

for name in names:
    if name[0:2] in specialfirstname:
        frequency[name[0:2]]=frequency.setdefault(name[0:2],0)+1
    else:
        frequency[name[0]]=frequency.setdefault(name[0],0)+1
result=dict(sorted(frequency.items(),key=lambda x: (-x[1],x[0])))
for item in result.items():
    print(f"{item[0]} {item[1]}")
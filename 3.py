mylist=[]
while True:
    thelist=input().split()
    if thelist==[]:
        break
    for i in thelist[1:]:
        mylist.append([thelist[0],i])
biglist=mylist.copy()
for i in range(len(mylist)):
    for j in range(len(mylist)):
        if mylist[j][-1]==mylist[i][0]:
            biglist[i]=biglist[j]+biglist[i][1:]
newlist=[]
for i in biglist:
    if i[-1].endswith(".py"):
        newlist.append(i)
for i in newlist:
    print("\\".join(i))
print(len(newlist))
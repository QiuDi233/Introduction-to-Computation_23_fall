dict_1={}
list_a=[]
while True:
    list_1=input().split()
    if len(list_1)>0:
        dict_1[list_1[0]]=list_1[1:]
        list_2=list_1[1:]
        for i in list_2:
            if i.endswith('.py'):
                list_a.append(i)
    else:
        break
num=len(list_a)
list_b=[]
for i in list_a:
    search=i
    re=i
    flag=True
    while flag:
        for k in dict_1.keys():
            for m in dict_1[k]:
                if m==search:
                    search=k
                    re=k+'\\'+re
                    break
        if search=='homework':
            break
    list_b.append(re)
for i in list_b:
    print(i)
print(str(num))
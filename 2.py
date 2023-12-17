import re
lst=[]
n=int(input())
for i in range(n):
    s=input()
    s_num=re.findall('<([1-9]\d{0,2}|0)>',s)
    if len(s_num)>0:
        lst.append(s_num)
    else:
        lst.append(['NONE'])
for i in lst:
    print(*i)
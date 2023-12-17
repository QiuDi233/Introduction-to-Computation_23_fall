num=int(input())
elder={}
non_elder={}
for _ in range(num):
    info=input().split(" ")
    if int(info[1])>=60:
        elder[info[0]]=int(info[1])
    else:
        non_elder[info[0]]=int(info[1])
sorted_elder=dict(sorted(elder.items(),key=lambda x:(-x[1])))
sorted_elder.update(non_elder)
for keys in sorted_elder:
    print(keys)
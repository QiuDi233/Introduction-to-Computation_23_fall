n=int(input())
lst=[]
for i in range(n):
    txt,pat=input().split()
    index=-1
    while True:
        index=txt.find(pat,index+1)
        if index==-1:
            break
        lst.append(index)
    if lst:
        for i in lst:
            print(i,end=' ')
    else:
        print('no')
    lst=[]
    print()
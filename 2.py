list=[int(x) for x in input().split()]
n,x,y=list[0],list[1],list[2]
if y/x==y//x:
    left=n-y//x
else:
   left=n-y//x-1
if left>=0:
    print(left)
else:
    print(0)
def check_num(n,k,s):
    num_set=set()
    for num in s:
        if k-num in num_set:
            return "yes"
        else:
            num_set.add(num)
    return "no"
n,k=map(int,input().split())
s=list(map(int,input().split()))
result=check_num(n,k,s)
print(result)
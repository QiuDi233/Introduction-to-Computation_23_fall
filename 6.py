def p_num(n):
    j=1
    for i in range (n-1):
        j=(j+1)*2
    return j

data_list=[]

m = int(input())
for _ in range(m):
    n = int(input())
    data_list.append(n)

for data in data_list:
    result=p_num(data)
    print(result)
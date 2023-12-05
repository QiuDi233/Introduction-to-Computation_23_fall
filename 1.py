n = int(input())
my_list = list(map(int,input().split()))
my_dict = {}
for i in range(n):
    if my_list[i] in my_dict.keys():
        my_dict[my_list[i]] += 1
    else:
        my_dict[my_list[i]] = 1
for i in range(n):
    if my_dict[my_list[i]] > 1:
        my_list[i] = n+1
x = min(my_list)
if x == n+1:
    print(-1)
else:
    print(my_list.index(x)+1)
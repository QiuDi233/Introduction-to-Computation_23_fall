my_list = list(input())
if my_list[len(my_list)-1] == 'X':
    my_list[len(my_list)-1] = '10'
my_list = [int(x) for x in my_list if x !='-']
sum_num = 0
for i in range(9):
    sum_num += my_list[i] * (i+1)
id = sum_num % 11
if id == my_list[9]:
    print('Right')
else:
    if id == 10:
        my_list[9] = 'X'
    else:
        my_list[9] = id
    my_list.insert(1,'-')
    my_list.insert(5,'-')
    my_list.insert(11,'-')
    for item in my_list:
        print(item,end='')
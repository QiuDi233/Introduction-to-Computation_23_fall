num = int(input())
i = 1
dict = {}

while i <= num:
    list = input().split()
    dict[(int(list[1]), int(list[2]))] = list[0]
    i = i+1

list2 = sorted(dict, reverse=True)
list3 = [dict.get(n) for n in list2]

m = 0
while m < num:
    print(list3[m])
    m = m+1
n, m = map(int, input().split())
book_to_people = {}
people_to_book = {}
for i in range(n):
    b = int(input())
    if b in book_to_people:
        book_to_people[b].append(i)
    else:
        book_to_people[b]=[i]
    people_to_book[i]=b
for i in range(n):
    b = people_to_book[i]
    friend = book_to_people[b]
    if len(friend) == 1:
        print('BeiJu')
    else:
        print(len(friend)-1)
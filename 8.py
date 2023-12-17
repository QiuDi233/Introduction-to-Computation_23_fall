n = int(input())

students = []

for i in range(n):
    scores = list(map(int, input().split()))
    total = sum(scores)
    students.append((i+1, total, scores[0]))

students.sort(key=lambda x: (-x[1], -x[2], x[0]))

for i in range(5):
    print(students[i][0], students[i][1])
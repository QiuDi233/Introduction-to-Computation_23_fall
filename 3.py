n = int(input())
distances = list(map(int, input().split()))

total_distance = 0
final_position = 0

for distance in distances:
    total_distance += abs(distance)

# 计算最终位置
final_position = sum(distances)

print(total_distance, final_position)
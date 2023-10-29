nums = int(input())
num1  = num3 = 0
for i in range(1, nums+1):
    num2 = 0
    for n in range(2, i+1):
        if i/n == int(i/n):
            num2 += i/n
    if num2 > i:
        num3 += 1
print(num3)
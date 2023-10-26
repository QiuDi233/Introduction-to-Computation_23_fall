# 描述
# 可以根据公式 π²/6 ≈ 1/1² + 1/2² + 1/3² + 1/4² + 1/5² + ... + 1/n² 来估算π的值。
# 现在给定一个实数ε (epsilon)，求出最小的值n，使得算出π的估算值的误差（即估算值与math.pi的差）的绝对值小于ε。
# 提示：使用while循环，每次n+=1，并在适当的条件下break。

# 输入
# 一个实数
# 输出
# 一个整数
# 样例输入
# 0.1
# 样例输出
# 10
import math
sum=0
n=1
epsilon=float(input())
while True:
    sum+=1/n**2
    pi = math.sqrt(6*sum)
    if abs(pi-math.pi)<epsilon:
        break
    n+=1
print(n)


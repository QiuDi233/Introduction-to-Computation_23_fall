# 05:寻找单身狗

# 总时间限制: 1000ms 内存限制: 65535kB
# 描述
# 在一个数组中有一个数字只出现一次，其它数字都出现2次，要求尽快找出这个数字。


# 输入
# 两行
# 第一行为整数n
# 第二行为n个整数
# 输出
# 单独存在的一个整数
# 样例输入
# 7
# 1 2 3 2 3 5 5
# 样例输出
# 1
# 来源
# 金华信奥熊老师

# 解法1:
n = int(input())
s = input().split()
for i in s:
    if s.count(i)==1:
        print(i)

# 解法2:
n = int(input())  
arr = list(map(int, input().split()))  
  
res = 0  
for num in arr:  
    res ^= num  
  
print(res)
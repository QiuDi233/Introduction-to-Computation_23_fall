# 描述
# 输入一行字符，统计出其中数字字符的个数。
#
# 输入
# 一行字符串，总长度不超过255。
# 输出
# 输出为1行，输出字符串里面数字字符的个数。
# 样例输入
# Peking University is set up at 1898.
# 样例输出
# 4

str=input()
sum=0
for s in str:
    if s.isdigit():
        sum+=1
print(sum)
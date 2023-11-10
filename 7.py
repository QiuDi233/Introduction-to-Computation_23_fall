# 7:统计字母
# 查看提交统计提问
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 统计一个字符串中的英文字母（区分大小写）出现频次，输出最高的频次及字母。字符串中可能出现的标点符号包括",.!&-"，单词之间有空格分隔。如果字母频次相同则按字母大小顺序排序（字母的ASCII码值可以采用ord()函数获得，'A'-'Z':65-90, 'a'-'z':97-122）。

# 输入
# 一段英文字母组成的字符串，其中存在标点符号
# 输出
# 出现频次最高的字母及频次，如有相同频次则按字母大小顺序排序输出。注意：字母、":"、频次之间没有空格！
# 样例输入
# Literally, the whole cloth here refers to cloth all in
# 样例输出
# e:7
# l:7
# 来源
# Wujj

n=input()
lst=[]
for i in range(len(n)):
    if n[i:i+1].isalpha():
        lst.append(n[i:i+1])
lst=list(set(lst))
lst1=[]
for i in range(len(lst)):
    num=n.count(lst[i])
    lst1.append([lst[i],num])
lst1=sorted(lst1,key=lambda x:(-x[1],x[0]))
num=lst1[0][1]
print(f"{lst1[0][0]}:{lst1[0][1]}")
for i in range(1,len(lst1)):
    if lst1[i][1]==num:
        print(f"{lst1[i][0]}:{lst1[i][1]}")
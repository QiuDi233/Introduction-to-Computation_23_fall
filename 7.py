s=input()
s=s.upper()
str1=s[0:1]
num=1
lst=[]
if len(s)==1:
    print(f"({str1},{num})")
else:
 for i in range(1,len(s)):
    if s[i:i+1]==str1 and i!=len(s)-1:
        num+=1
    elif s[i:i+1]!=str1 and i!=len(s)-1:
        lst.append((str1,num))
        str1=s[i:i+1]
        num=1
    elif s[i:i + 1] == str1 and i == len(s) - 1:
        num+=1
        lst.append((str1,num))
    elif s[i:i+1]!=str1 and i==len(s)-1:
        lst.append((str1,num))
        str1 = s[i:i + 1]
        num = 1
        lst.append((str1,num))
for i in lst:
    print(f"({i[0]},{i[1]})",end="")
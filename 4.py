n=int(input())
original=[]
totalist=[]
wordict={}
seqdict={}
for _ in range(n):
    line=list(map(str,input().split()))
    original.append(line)
    for l in line:
        totalist.append(l)
for x in totalist:
    wordict[x]=totalist.count(x)
seq=list(wordict.items())
seq.sort(key=lambda x:x[0])
seq.sort(key=lambda x:x[1])
num=list(enumerate(seq))
for s in num:
    seqdict[s[1][0]]=s[0]
for a in range(n):
    linelist=[]
    for b in range(len(original[a])):
        original[a][b]=seqdict[original[a][b]]
        linelist.append(str(original[a][b]))
        s=' '.join(linelist)
    print(s)
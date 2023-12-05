x,y=map(int,input().split())
n=input()
hash_1=0
for i in range(0,len(n)):
    hash_1=hash_1+ord(n[i])*x**i
hash_2=hash_1%y
print(hash_2)
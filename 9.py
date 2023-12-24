n=int(input())
if n==1:
    print("End")
while n!=1:
    if n%2==0:
       n=n/2
       a=2*n
       print(int(a),"/2=",int(n),sep='')
    else:
        print(int(n),"*3+1=",3*int(n)+1,sep='')
        n=3*n+1
        
    if n==1:
        print("End")
        break

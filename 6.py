res = {}
def recursion(n):
    if n in res:
        return res[n]
   
    if n == 0:
        return 1
 
    else:
        result = recursion(n//2) + recursion(n//3)
        res[n] = result
        return result
a=int(input())
print(recursion(a))
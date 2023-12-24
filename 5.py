nums=input().split()
nums=[int(a) for a in nums]
n=nums[0]
list1=[]
for a in range(2,n+1):
    b=abs(nums[a]-nums[a-1])
    list1.append(b)
if set(list1)==set(a for a in range(1,n)):
    print("Jolly")
else:
    print("Not jolly")
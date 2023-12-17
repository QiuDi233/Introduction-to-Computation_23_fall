n=int(input())
for i in range(n):
    total=int(input())
    solutions=[]
    for c in range((total//2)+1):
        r=total-2*c
        if r%4==0:
            solutions.append((c,r//4))
    if solutions==[]:
        print("0 0")
    else:
        minsolution=solutions[0][0]+solutions[0][1]
        maxsolution=solutions[0][0]+solutions[0][1]
        for i in range(len(solutions)):
            minsolution=min(minsolution,solutions[i][0]+solutions[i][1])
            maxsolution=max(maxsolution,solutions[i][0]+solutions[i][1])
        print(minsolution,maxsolution)
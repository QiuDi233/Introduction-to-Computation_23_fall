m,n=map(int,input().split())
course_list=[]
for i in range(m):
    course=input().split()
    course_list.append([course[0],int(course[1])])
student_list=[]
for t in range(n):
    code,*choice=input().split()
    student_list.append([code,choice])
final_dict={}
for cour in course_list:
    cour_list=[]
    for stud in student_list:
        if cour[0] in stud[1]:
            x=stud[1].index(cour[0])
            cour_list.append([int(stud[1][x+1]),int(stud[0])])
        else:
            pass
    cour_list=sorted(cour_list,reverse=True)
    c_list=[c[1] for c in cour_list]
    final_dict[cour[0]]=c_list[0:cour[1]] if len(c_list)>=cour[1] else c_list
query=list(map(int,input().split()))
for q in query:
    qlist=[]
    for key in final_dict.keys():
        if q in final_dict[key]:
            qlist.append(key)
    if not qlist:
        print("None")
    else:
        print(" ".join(qlist))
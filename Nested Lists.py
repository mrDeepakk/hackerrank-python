n=int(input())
result=[]
grade=[]
for i in range (n):
    name=input()
    score=float(input())
    result.append([name,score])
    grade.append(score)
sl=(sorted(set(grade)))[1]
for i,j in sorted(result):
    if j==sl:
        print(i)
from itertools import count


n=int(input())
a=list()
b=list()
for i in range(n):
    a.append(input())
print(len(set(a)))
for i in set(a):
    c=a.count(i)
    b.append(c)

s=sorted(b)
for i in range(len(b),0,-1):
    print(b[i-1],end=" ")
    

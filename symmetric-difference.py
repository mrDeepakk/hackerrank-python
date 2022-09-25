
n1=int(input())
s1=list(map(int,input().split()))
n2=int(input())
s2=list(map(int,input().split()))

for i in range(len(s1)-1):
    temp=s1[i]
    if s1[i] in s2:
        s1.remove(s1[i])
        s2.remove(s1[i])

for i in s1:
    print(i)
for i in s2:
    print(i)
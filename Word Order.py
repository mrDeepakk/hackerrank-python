from typing import OrderedDict
d=OrderedDict()
lis=list()
n=int(input())
for i in range(n):
    temp=input()
    d[temp]=d.get(temp,0)+1
print(len(d))
for i in d:
    print(d[i],end=" ")

from collections import defaultdict
from collections import defaultdict

d=defaultdict(list)
n,m = map(int, input().split())
for i in range(1,n+1):
    item=input()
    d[item].append(i)

for i in range(m):
    key=input()
    if key in d:
        print(*d[key])
    else:
        print(-1)
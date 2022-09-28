n=int(input())
s=set(map(int,input().split()))
n2=int(input())
for i in range(n2):
    d=input()
    if d=='pop':
        s.pop()
    elif d[:-2]=='discard':
        s.discard(int(d[-1]))
    elif d[:-2]=='remove':
        s.remove(int(d[-1]))

print(s)
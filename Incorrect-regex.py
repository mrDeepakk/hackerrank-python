import re
n1=int(input())
s1=list()
for i in range(n1):
    s1.append(input())

for i in s1:
    try:
        print(bool(re.compile(i)))
    except re.error:
        print(False)
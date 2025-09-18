# cook your dish here
from collections import Counter
t=int(input())
for i in range(t):
    f=list(map(str,input().split()))
    x=list(map(str,input().split()))
    freq=Counter(f)
    freq1=Counter(x)
    a=freq+freq1
    seen=set()
    for j in a:
        if a[j]==2:
            seen.add(j)
            break
    print(j)

# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    s=min(a,b)
    b=max(a,b)
    while s<b:
        s*=2
    if s==b:
        print("YES")
    else:
        print("NO")

# cook your dish here
t=int(input())
for i in range(t):
    r1,r2,r3,r4=(map(int,input().split()))
    a=r1+r2
    b=r2+r3
    c=r3+r4
    d=r4+r1
    e=r1+r3
    f=r2+r4
    maximum=max(a,b,c,d,e,f)
    if maximum==0:
        print("IN")
    else:
        print("OUT")

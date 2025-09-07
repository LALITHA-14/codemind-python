# cook your dish here
t=int(input())
for i in range(t):
    q,p=map(int,input().split())
    total=q*p
    if q>1000:
        total=total*0.9
    print("{:.6f}".format(total))

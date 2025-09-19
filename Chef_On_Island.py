# cook your dish here
t=int(input())
for i in range(t):
    x,y,xr,yr,d=map(int,input().split())
    a1=x/xr 
    b1=y/yr 
    c=min(a1,b1)
    if(c>=d):
        print("YES")
    else:
        print("NO")

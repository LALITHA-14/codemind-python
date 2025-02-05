# cook your dish here
t=int(input())
for i in range(t):
    x1,x2,y1,y2,z1,z2=map(int,input().split())
    if(x1>x2 or y1>y2 or z2>z1):
        print("NO")
    else:
        print("YES")

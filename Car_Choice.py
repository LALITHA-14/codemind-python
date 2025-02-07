# cook your dish here
t=int(input())
for i in range(t):
    x1,x2,y1,y2=map(int,input().split())
    a=y1/x1
    b=y2/x2
    if(a<b):
        print(-1)
    elif(a==b):
        print(0)
    else:
        print(1)

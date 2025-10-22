# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    se=0
    so=0
    for j in range(x,y+1):
        if j%x==0 and j%2==0:
            se+=j 
        elif j%x==0 and j%2==1:
            so+=j 
    if se>=so:
        print("YES")
    else:
        print("NO")

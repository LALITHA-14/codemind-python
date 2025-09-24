# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if (x+y)%3==0:
        print(((x+y)//3)+min((x+y)//3,y))

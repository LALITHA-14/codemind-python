# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    b=(y-x)//2
    a=x+b
    print(a,b)

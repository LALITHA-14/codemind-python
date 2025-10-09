# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    n=(x+y)+abs(x-y)-1
    if n%2==0:
        n-=1 
    print(n)

# cook your dish here
t=int(input())
for i in range(t):
    n,k,x,y=map(int,input().split())
    blue_lamp=n-k
    blue_cost=min(x,y)
    print((k*x)+(blue_lamp)*(blue_cost))
    

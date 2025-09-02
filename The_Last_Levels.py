# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    total_time=x*y 
    breaks=x//3
    if x%3==0:
        breaks-=1
    total_time+=breaks*z 
    print(total_time)

# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    a1=x*y
    a2=y*z 
    a3=x*z 
    b1=z 
    b2=x
    b3=y
    if a1%b1==0 :
        print(f"{a1} {b1}")
    elif a2%b2==0:
        print(f"{a2} {b2}")
    elif a3%b3==0:
        print(f"{a3} {b3}")
    else:
        print(-1)

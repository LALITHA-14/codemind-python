# cook your dish here
t=int(input())
for i in range(t):
    x,y,p,q=map(int,input().split())
    a=x+(p*10)
    b=y+(q*10)
    if(a<b):
        print("Chef")
    elif(b<a):
        print("Chefina")
    else:
        print("Draw")

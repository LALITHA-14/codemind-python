# cook your dish here
t = int(input())
for i in range(t):
    a,x,b,y = map(int,input().split())
    if(a*y==b*x):
        print("Equal")
    elif(a*y<b*x):
        print("Bob")
    else:
        print("Alice")
    

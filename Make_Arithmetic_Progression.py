# cook your dish here
t = int(input())
for i in range(t):
    x,y,z = map(int,input().split())
    a = y-x
    b = z-y
    c = 0 
    if(a!=b):
        c+=1
    else:
        c=0
    print(c)
    

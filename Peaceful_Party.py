# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if (a+c)>b:
        print((a+c))
    else:
        print(b)
        

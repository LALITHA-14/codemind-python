# cook your dish here
t=int(input())
for i in range(t):
    n,x,k=map(int,input().split())
    if((k//x)<n):
        print(k//x)
    else:
        print(n)

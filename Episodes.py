# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=n*k 
    print(a//60,a%60)

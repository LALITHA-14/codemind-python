# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    ans=2*n-x+1
    print(ans)

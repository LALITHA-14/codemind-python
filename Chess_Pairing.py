# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    print(max(0,(2*x)-(2*n)))

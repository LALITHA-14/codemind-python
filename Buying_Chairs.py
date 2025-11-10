# cook your dish here
t=int(input())
for i in range(t):
    w,p,k=map(int,input().split())
    print(k+min(w,k))

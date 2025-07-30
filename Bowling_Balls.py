# cook your dish here
t=int(input())
for i in range(t):
    n,x,y=map(int,input().split())
    arr=list(map(int,input().split()))
    c=0
    for j in range(len(arr)):
        if arr[j]>=x and arr[j]<=y:
            c+=1
    print(c)

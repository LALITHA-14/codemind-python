# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    s=0
    for j in range(len(arr)):
        s+=arr[j]
    if s==n:
        print(max(arr))

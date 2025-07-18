# cook your dish here
t=int(input())
for i in range(t):
    c=0
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(len(arr)):
        if arr[i]>=1000:
            c+=1
    print(c)

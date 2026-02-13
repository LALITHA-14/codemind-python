# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if (sum(arr))%2==0:
        print("Yes")
    else:
        print("No")

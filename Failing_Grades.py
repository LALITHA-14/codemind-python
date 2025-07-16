# cook your dish here
t = int(input())
for i in range(t):
    sums=0
    success=True
    n=int(input())
    arr=list(map(int,input().split()))
    for j in range(n):
        sums+=arr[j]
        avg=sums/(j+1)
        if avg<40:
            success=False
            break
    print("Yes" if success else "No")

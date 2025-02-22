# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    min_slices=10*n
    max_slices=12*n
    if(min_slices<=k<=max_slices):
        print("YES")
    else:
        print("NO")

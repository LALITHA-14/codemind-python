t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    a = n/m
    if(a%2==0):
        print("Yes")
    else:
        print("No")

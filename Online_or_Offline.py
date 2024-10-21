# cook your dish here
t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    a = n - ((0.1)*n)
    if(a==m):
        print("EITHER")
    elif(a>m):
        print("DINING")
    else:
        print("ONLINE")

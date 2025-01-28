# cook your dish here
t = int(input())
for i in range(t):
    m,n,k = map(int,input().split())
    a = n * k 
    if(m>a):
        print("YES")
    else:
        print("NO")

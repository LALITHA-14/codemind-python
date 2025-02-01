# cook your dish here
t = int(input())
for i in range(t):
    z,y,a,b,c = map(int,input().split())
    spent = z-y
    total = a+b+c
    if(spent>=total):
        print("YES")
    else:
        print("NO")

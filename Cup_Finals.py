# cook your dish here
t = int(input())
for i in range(t):
    x,y,d = map(int,input().split())
    a = x - y
    if(abs(a)<=d):
        print("YES")
    else:
        print("NO")

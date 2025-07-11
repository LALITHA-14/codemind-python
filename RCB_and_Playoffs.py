# cook your dish here
t = int(input())
for i in range(t):
    x, y, z = map(int,input().split())
    if x+(2*z)>=y:
        print("YES")
    else:
        print("NO")

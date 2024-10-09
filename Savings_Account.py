# cook your dish here
t = int(input())
for i in range(t):
    x,y,z = list(map(int,input().split()))
    if x * y <= z:
        print(0)
    else:
        k = (x * y - z + y - 1)//y
        print(k)

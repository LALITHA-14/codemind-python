# cook your dish here
t = int(input())
for i in range(t):
    w,x,y,z = map(int,input().split())
    if((x+y)==w or (y+z)==w or (z+x)==w or x==w or y == w or z==w or (x+y+z)==w):
        print("YES")
    else:
        print("NO")

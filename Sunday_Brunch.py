t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    print(min(20,x//y))

t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    d = b/a
    if(d<c):
        print("%d"%(c-d))
    else:
        print(0)

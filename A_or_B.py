# cook your dish here
t = int(input())
for i in range(t):
    x, y = map(int,input().split())
    solved_time = x+y
    a = 500 - (x*2)
    b = 1000 - (solved_time*4)
    c = 1000 - (y*4)
    d = 500 - (solved_time * 2)
    if((a+b)>=(c+d)):
        print(a+b)
    else:
        print(c+d)

# cook your dish here
t = int(input())
for i in range(t):
    x, m, d = map(int,input().split())
    a = x * m
    b = x + d
    print(min(a,b))

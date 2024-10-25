# cook your dish here
t = int(input())
for i in range(t):
    n, x, d = map(int,input().split())
    a = x*5
    b = n//a
    print(d+b)

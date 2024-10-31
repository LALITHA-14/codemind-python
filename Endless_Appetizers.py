# cook your dish here
import math
t = int(input())
for i in range(t):
    x, y, r = map(int,input().split())
    a = r//30
    b = x+a
    print(math.ceil(b/y))
    

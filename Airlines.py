# cook your dish here
import math
t = int(input())
for i in range(t):
    x, n = map(int,input().split())
    a = x*100
    if(a>=n):
        print(0)
    else:
        b = math.ceil(n/100)
        print(b-x)
        

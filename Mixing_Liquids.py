# cook your dish here
import math
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    # for ratio given 1:2 the values will be x, 2x and the total will be x+2x=3x
    x = min(a,b//2) # x<=a, 2x<=b
    m = 2*x 
    total=x+m 
    print(total)

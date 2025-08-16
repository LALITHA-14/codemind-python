# cook your dish here
import math
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    res=math.ceil(abs(x-y)/2)
    print(res)

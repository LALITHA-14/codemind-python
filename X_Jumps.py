# cook your dish here
import math
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print((x//y)+(x%y))

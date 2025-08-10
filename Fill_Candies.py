# cook your dish here
import math
t=int(input())
for i in range(t):
    n,k,m=map(int,input().split())
    s=k*m
    p=n/s
    a=math.ceil(p)
    st=math.ceil(a)
    print(st)

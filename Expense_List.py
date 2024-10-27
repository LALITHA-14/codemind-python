# cook your dish here
import math
t = int(input())
for i in range(t):
    n, x = map(int,input().split())
    print(2**(x-n))

# cook your dish here
r,o,c=map(int,input().split())
overs=20-o
a=overs*6
b=a*6
s=c+b
if s>r:
    print("YES")
else:
    print("NO")

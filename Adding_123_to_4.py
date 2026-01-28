# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    pairs_13 = min(x, z)     # (1,3) pairs
    pairs_22 = y // 2        # (2,2) pairs
    print(pairs_13 + pairs_22)

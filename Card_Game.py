def count_ways(n, x):
    if n%2==0:
        ec = n//2
        oc = n//2
    else:
        ec = n//2
        oc = n//2+1
    if x%2==0:
        return ec-1
    else:
        return oc-1
t = int(input())
for i in range(t):
    n, x = map(int,input().split())
    print(count_ways(n, x))

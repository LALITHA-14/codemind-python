# cook your dish here
t=int(input())
for i in range(t):
    r,b,g=map(int,input().split())
    bundles=min(r,b,g)
    coins = bundles * 10 + (r + b + g - 3 * bundles) * 3
    print(coins)

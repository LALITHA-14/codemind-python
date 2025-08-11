# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    total_calories=0
    sweets_eaten=0
    for calories in arr:
        if total_calories+calories<=k:
            total_calories+=calories
            sweets_eaten+=1
        else:
            break
    print(sweets_eaten)

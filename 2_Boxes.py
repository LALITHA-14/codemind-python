# cook your dish here
t=int(input())
for i in range(t):
    x,y,K=map(int,input().split())
    diff=abs(x-y)
    if diff==K:
        print("0")
    elif (diff>K and (diff-K)%2==0) or (diff<K and (K-diff)%2==0):
        print(abs(diff-K)//2)
    else:
        print("-1")

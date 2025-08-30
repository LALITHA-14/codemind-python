# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    rev=0
    av=n
    while(n!=0):
        rev=(rev*10)+(n%10)
        n=n//10
    if av==rev:
        print("wins")
    else:
        print("loses")

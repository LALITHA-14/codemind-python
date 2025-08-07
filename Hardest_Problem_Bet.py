# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    hardest=min(a,b,c)
    if hardest==a:
        print("Draw")
    elif hardest==b:
        print("Bob")
    elif hardest==c:
        print("Alice")

# cook your dish here
t=int(input())
for i in range(t):
    p,q=map(int,input().split())
    total_points=(p+q)//2
    if total_points%2==0:
        print("Alice")
    else:
        print("Bob")

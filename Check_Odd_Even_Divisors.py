# cook your dish here
t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    if a==0:
        print("No")
    elif b%a==0:
        print("Yes")
    else:
        print("No")

# cook your dish here
t=int(input())
for i in range(t):
    a,b = map(int,input().split())
    c=a+b
    if(c%2==0):
        print("Bob")
    else:
        print("Alice")

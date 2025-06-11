# cook your dish here
t = int(input())
for i in range(t):
    x=int(input())
    while x>3 or x%2==0:
        if x>3:
            x=x-3
        elif x%2==0:
            x=x//2
    print(x)

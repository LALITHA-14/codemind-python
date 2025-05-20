# cook your dish here
t = int(input())
for i in range(t):
    n,x,y,a,b = map(int,input().split())
    petrol=(n/a)*x
    diesel=(n/b)*y
    if diesel<petrol:
        print("DIESEL")
    elif petrol<diesel:
        print("PETROL")
    else:
        print("ANY")
    

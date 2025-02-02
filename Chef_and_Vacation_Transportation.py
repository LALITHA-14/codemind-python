# cook your dish here
t = int(input())
for i in range(t):
    x,y,z = map(int,input().split())
    a = x+y
    if(a>z):
        print("TRAIN")
    elif(a<z):
        print("PLANEBUS")
    else:
        print("EQUAL")


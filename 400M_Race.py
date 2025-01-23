t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    # your code goes here
    a = 400/x
    b = 400/y
    c = 400/z
    if(a>b and a>c):
        print("ALICE")
    elif(b>a and b>c):
        print("BOB")
    elif(c>a and c>b):
        print("CHARLIE")

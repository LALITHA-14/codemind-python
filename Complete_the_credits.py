# cook your dish here
t = int(input())
for i in range(t):
    x = int(input())
    if(x>65):
        print("Overload")
    elif(x<35):
        print("Underload")
    else:
        print("Normal")

# cook your dish here
t = int(input())
for i in range(t):
    x = int(input())
    if(x%10==0):
        print(x//10)
    elif(x%5==0):
        print((x//10)+1)
    else:
        print(-1)

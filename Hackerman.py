t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    c = a+b
    count = 0
    for j in range(1, c+1):
        if(c%j==0):
            count+=1
    if(count==2):
        print("Alice",sep = " ")
    else:
        print("Bob",sep = " ")

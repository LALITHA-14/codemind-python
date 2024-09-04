t = int(input())
for i in range(t):
    a1,a2,b1,b2 = map(int,input().split())
    a = a1-a2
    b = b1-b2
    n = a+b
    if(-(n)>0):
        print("YES", sep= " ")
    else:
        print("NO", sep=" ")
    

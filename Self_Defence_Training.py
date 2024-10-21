# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    c=0
    for j in range(n):
        if(lst[j]>=10 and lst[j]<=60):
            c+=1
    print(c)

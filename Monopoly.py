# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    company_1=b+c+d
    company_2=a+c+d 
    company_3=a+b+d 
    company_4=a+b+c
    if a>company_1 or b>company_2 or c>company_3 or d>company_4:
        print("YES")
    else:
        print("NO")

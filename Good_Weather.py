# cook your dish here
t=int(input())
for i in range(t):
    a1,a2,a3,a4,a5,a6,a7=map(int,input().split())
    a=a1+a2+a3+a4+a5+a6+a7
    if(a>=4):
        print("YES")
    else:
        print("NO")

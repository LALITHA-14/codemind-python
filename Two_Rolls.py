# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    min_pos=x+2*y  
    max_pos=x+2*(y+5)
    if min_pos<=50<=max_pos:
        print("Yes")
    else:
        print("No")
   

# cook your dish here
import math
t = int(input())
for i in range(t):
    n = int(input())
    if(n%10==0):
        print(100-n)
    else:
        if(n%10>=5):
            rounded_cost = n+(10-(n%10)) # Round up
        else:
            rounded_cost = n-(n%10) # Round down
        print(100-rounded_cost)

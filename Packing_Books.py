# cook your dish here
import math
t = int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    boxes=math.ceil(y/z)
    total_number_of_boxes=x*boxes
    print(total_number_of_boxes)

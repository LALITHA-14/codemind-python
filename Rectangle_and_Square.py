# cook your dish here
a, b, c = map(int,input().split())
area_of_rectangle = a*b
area_of_square = c*c
if(area_of_rectangle==area_of_square):
    print("Yes")
else:
    print("No")

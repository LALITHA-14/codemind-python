# cook your dish here
l=int(input())
b=int(input())
area=l*b
perimeter=2*(l+b)
if(area>perimeter):
    print("Area")
    print(area)
elif(perimeter>area):
    print("Peri")
    print(perimeter)
else:
    print("Eq")
    print(area)

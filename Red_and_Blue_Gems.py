# cook your dish here
r, b, p, q = map(int,input().split())
red = r*p
blue = b*q
if red>=blue:
    print(red)
else:
    print(blue)

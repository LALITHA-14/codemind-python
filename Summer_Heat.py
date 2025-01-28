# cook your dish here
t = int(input())
for i in range(t):
    xa, xb, Xa, Xb = map(int,input().split())
    a = Xa//xa
    b = Xb//xb
    ty = a+b
    print(ty)

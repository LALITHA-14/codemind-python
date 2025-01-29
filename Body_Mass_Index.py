# cook your dish here
t = int(input())
for i in range(t):
    m, h = map(int,input().split())
    a = m//(h*h)
    if(a<=18):
        print(1)
    elif(a>=19 and a<=24):
        print(2)
    elif(a>=25 and a<=29):
        print(3)
    else:
        print(4)

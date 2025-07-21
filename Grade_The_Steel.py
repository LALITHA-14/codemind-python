# cook your dish here
t=int(input())
for i in range(t):
    ha,ca,te=input().split()
    ha=int(ha)
    ca=float(ca)
    te=int(te)
    if ha>50 and ca<0.7 and te>5600:
        print(10)
    elif ha>50 and ca<0.7:
        print(9)
    elif ca<0.7 and te>5600:
        print(8)
    elif ha>50 and te>5600:
        print(7)
    elif ha>50:
        print(6)
    elif ca<0.7:
        print(6)
    elif te>5600:
        print(6)
    else:
        print(5)

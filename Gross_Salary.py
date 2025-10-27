# cook your dish here
t=int(input())
for i in range(t):
    hra=0 
    da=0
    salary=int(input())
    if salary<1500:
        hra=(10/100)*salary
        da=(90/100)*salary
    else:
        hra=500 
        da=(98/100)*salary
    print(salary+hra+da)

# cook your dish here
n = int(input())
a=1
for i in range(10,0,-1):
    if(n%i==0):
        a=i
        break
print(a)

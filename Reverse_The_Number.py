# cook your dish here
t=int(input())
for i in range(t):
    rev=0
    n=int(input())
    while(n!=0):
        rev=(rev*10)+(n%10)
        n=n//10
    print(rev)

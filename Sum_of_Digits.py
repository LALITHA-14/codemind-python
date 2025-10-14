# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    current_sum=0
    while(n>0):
        digit=n%10
        current_sum+=digit
        n=n//10
    print(current_sum)

# cook your dish here
t = int(input())
for i in range(t):
    n=int(input())
    odd_divisors=0
    even_divisors=0
    for j in range(1,n+1):
        if n%j==0 and j%2!=0:
            odd_divisors+=1
    for j in range(1,n+1):
        if n%j==0 and j%2==0:
            even_divisors+=1
    print(odd_divisors,even_divisors)

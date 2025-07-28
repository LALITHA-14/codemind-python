# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    sub=n-1
    add=n-2
    number=n+sub+add
    final = 2*(max(n,sub,add))
    if final<number:
        print(number)
    else:
        print(-1)

# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    sa=[6,13,20,27]
    su=[7,14,21,28]
    print(len(set(arr+sa+su)))

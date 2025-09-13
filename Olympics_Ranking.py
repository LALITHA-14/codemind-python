# cook your dish here
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    split_index=len(a)//2
    first_part=a[:split_index]
    last_part=a[split_index:]
    s1=0
    s2=0
    for j in range(len(first_part)):
        s1+=first_part[j]
    for k in range(len(last_part)):
        s2+=last_part[k]
    if s1>s2:
        print(1)
    else:
        print(2)

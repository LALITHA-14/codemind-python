#User function Template for python3
n = int(input())
# Your code here
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(True)
else:
    print(False)

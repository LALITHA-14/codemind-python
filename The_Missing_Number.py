# Enter your code here. Read input from STDIN. Print output to STDOUT
arr=list(map(int,input().split()))
n=len(arr)
print(n*(n+1)//2+len(arr)+1-sum(arr))

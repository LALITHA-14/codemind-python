# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
mean=round(sum(arr)/len(arr),2)
median=0
if n%2!=0:
    median=round(arr[n//2],2)
else:
    median=round((arr[n//2-1]+arr[n//2])/2,2)
freq=Counter(arr)
max_freq=max(freq.values())
mode=min([k for k,v in freq.items() if v==max_freq])
print("{:.2f}".format(mean),"{:.2f}".format(median),mode)

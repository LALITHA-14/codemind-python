#User function Template for python3
class Solution:
    def repeatedSumOfDigits (self,N):
        # code here 
        seen=set()
        while(N>=10):
            seen.add(N)
            N=sum(int(i) for i in str(N))
        return N
            

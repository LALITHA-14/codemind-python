#User function Template for python3
class Solution:
    def isHappy (self, N):
        # code here
        seen=set()
        while N!=1 and N not in seen:
            seen.add(N)
            N=sum(int(i)**2 for i in str(N))
        if N==1:
            return 1
        return 0

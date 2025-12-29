#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a1=Counter(a)
        b1=Counter(b)
        for i in b1:
            if b1[i]>a1.get(i,0):
                return False
        return True
    
    
    

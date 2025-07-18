# User function Template for python3
from collections import Counter
class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        #code here
        a1=Counter(a)
        b1=Counter(b)
        return a1==b1

#User function Template for python3
class Solution:
    def intersection(self, a, b):
        # Your code here
        a1=set(a)
        b1=set(b)
        return sorted(a1.intersection(b1))

class Solution:
    def findUnion(self, a, b):
        # code here 
        a1=set(a)
        b1=set(b)
        res=a1.union(b1)
        return sorted(res)

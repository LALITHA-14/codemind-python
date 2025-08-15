class Solution:
    def kthElement(self, a, b, k):
        # code here
        res=sorted(a+b)
        for i,res in enumerate(res,start=1):
            if i==k:
                return res

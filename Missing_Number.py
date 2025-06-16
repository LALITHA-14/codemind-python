class Solution:
    def missingNum(self, arr):
        # code here
        n= len(arr)+1
        total = n*(n+1)//2
        return total-sum(arr)

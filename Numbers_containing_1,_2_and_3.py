class Solution:
    def filterByDigits(self, arr):
        #code here
        res=[]
        for num in arr:
            string=str(num)
            if all(ch in '123' for ch in string):
                res.append(num)
        return res if res else [-1]

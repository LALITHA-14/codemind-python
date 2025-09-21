# User function template for Python 
class Solution:
    def findMagicalNumber(self, arr):
        # code here
        for i in range(len(arr)):
            if arr[i]==i:
                return arr[i]
        return -1

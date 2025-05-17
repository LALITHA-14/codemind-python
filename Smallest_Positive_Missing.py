#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr.sort()
        res=1
        for num in arr:
            if num==res:
                res+=1
            elif num>res:
                break
        return res

#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #code here
        arr.sort()
        candidate=arr[len(arr)//2] # For middle element
        if arr.count(candidate)>len(arr)//2:
            return candidate
        return -1

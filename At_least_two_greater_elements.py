#User function Template for python3

class Solution:
    def findElements(self,arr):
        # Your code goes here
        arr.sort(reverse=True)
        return sorted(arr[2:])

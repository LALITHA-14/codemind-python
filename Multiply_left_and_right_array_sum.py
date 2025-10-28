#User function Template for python3

class Solution:
    def multiply(self, arr):
        # Code here
        k=len(arr)//2
        first=sum(arr[:k])
        second=sum(arr[k:])
        return first*second

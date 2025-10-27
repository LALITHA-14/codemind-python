class Solution:
    def areConsecutives(self, arr):
        # Your code goes here
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]!=1:
                return False
        return True

#User function Template for python3

class Solution:
    def countOfElements(self, x, arr):
        # Code Here
        c=0
        for i in range(len(arr)):
            if arr[i]<=x:
                c+=1
        return c


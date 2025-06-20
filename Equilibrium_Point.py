# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        total_sum=sum(arr)
        left_sum=0
        for i in range(len(arr)):
            if left_sum==total_sum-left_sum-arr[i]:
                return i
            left_sum+=arr[i]
        return -1


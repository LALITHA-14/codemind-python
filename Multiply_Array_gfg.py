#User function Template for python3

class Solution:
    def longest(self, arr, n):
        #Code Here
        p=1
        for i in range(n):
            p*=arr[i]
        return p

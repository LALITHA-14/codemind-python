#User function Template for python3

class Solution:
    def maxValue(self, arr): 
        # Complete the function
        arr.sort()
        pro=1
        sums=0
        for i in range(len(arr)):
            pro=i*arr[i]
            sums+=pro
        return sums%(10**9+7)

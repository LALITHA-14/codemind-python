class Solution:
    # arr is the array
    def product(self, arr):
        # your code here
        pro=1
        for i in range(len(arr)):
            pro*=arr[i]
        if pro<1000000007:
            return pro
        return pro%1000000007

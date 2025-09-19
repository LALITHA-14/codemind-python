#User function Template for python3

class Solution:
    def customSort(self, arr):
        # code here
        s=len(arr)//2
        first=arr[:s]
        second=arr[s:]
        first.sort()
        second.sort(reverse=True)
        return first+second


class Solution:
    def swapKth(self, arr, k):
        # Code Here
        n=len(arr)
        start_index=k-1 # Converting into 0-indexing
        end_index=n-k # kth element from the end
        arr[start_index],arr[end_index]=arr[end_index],arr[start_index]
        return arr

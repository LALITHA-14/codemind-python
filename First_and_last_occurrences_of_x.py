# User function Template for python3
class Solution: 
    def firstAndLast(self, x, arr): 
        n = len(arr)
        
        # ----- First occurrence -----
        low, high = 0, n - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                first = mid
                high = mid - 1   # keep searching left
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        # ----- Last occurrence -----
        low, high = 0, n - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                last = mid
                low = mid + 1    # keep searching right
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        if first == -1:   # element not found
            return [-1]
        else:
            return [first, last]

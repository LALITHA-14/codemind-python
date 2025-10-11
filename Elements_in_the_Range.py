class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        arr.sort()
        c=0
        for i in range(A,B+1):
            if i not in arr:
                return False
        return True

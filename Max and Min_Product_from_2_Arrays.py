#User function Template for python3

class Solution:
    # Function to find the maximum element from array arr1 and 
    # the minimum element from array arr2 and return their product.
    def find_multiplication(self, arr1, arr2):
        # code here
        maximum_arr1=max(arr1)
        minimum_arr2=min(arr2)
        return maximum_arr1*minimum_arr2

#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        result=sorted(arr1+arr2)
        mid1=(len(result))//2-1
        mid2=(len(result))//2
        return result[mid1]+result[mid2]

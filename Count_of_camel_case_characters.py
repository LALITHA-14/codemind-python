#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        # your code here
       return sum('A'<=ch<='Z' for ch in s)

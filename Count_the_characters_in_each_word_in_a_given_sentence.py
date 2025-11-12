#User function Template for python3

class Solution:
    def countChars(self,s):
        # code here 
        words=s.split()
        result=[len(word) for word in words]
        return result

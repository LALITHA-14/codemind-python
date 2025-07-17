#User function Template for python3

class Solution:

    def amendSentence(self, s):

        # code here
        result=''
        for i in range(len(s)):
            if s[i].isupper() and i!=0:
                result+=' '
            result+=s[i].lower()
        return result

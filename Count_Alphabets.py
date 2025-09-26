#User function Template for python3
import re
class Solution:

    def Count(self, S):
        # code here
        a=re.sub(r'[!@#$%^&*0-9]','',S)
        return len(a)

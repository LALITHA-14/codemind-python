# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        #code here
        return set(s)<={'0','1'}

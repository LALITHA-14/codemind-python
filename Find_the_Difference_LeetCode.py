from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1=Counter(s)
        t1=Counter(t)
        for i in t1:
            if t1[i]!=s1.get(i,0):
                return i

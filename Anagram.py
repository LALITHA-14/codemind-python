class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       return sorted(s1)==sorted(s2)

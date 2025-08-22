class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original = x
        reverse = 0
        while x>0:
            reverse = reverse*10 + (x%10)
            x = x//10
        if reverse == original:
            return True
        return False

class Solution:
    def checkStatus(self, a, b, flag):
        # Case 1: exactly one is non-negative AND flag is False
        if ((a >= 0 and b < 0) or (a < 0 and b >= 0)) and (flag == False):
            return True
        # Case 2: both are negative AND flag is True
        elif (a < 0 and b < 0) and (flag == True):
            return True
        else:
            return False

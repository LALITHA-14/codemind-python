#User function Template for python3


class Solution:

    def oddAndEven(self, S):
        odd, even = 0, 0
        for i in range(len(S)):
            if i % 2:
                even += int(S[i])
            else:
                odd += int(S[i])
        return 1 if even == odd else 0

class Solution:
    def ExtractNumber(self, sentence):
        parts = sentence.split()
        ans = -1
        for word in parts:
            if word.isdigit():                 # check if it's a number
                if '9' not in word:            # ignore numbers containing 9
                    ans = max(ans, int(word))  # keep track of largest
        return ans

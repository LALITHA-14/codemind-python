class Solution:
    def reverseWords(self, s: str) -> str:
        #code here
        return ' '.join(word[::-1] for word in s.split())

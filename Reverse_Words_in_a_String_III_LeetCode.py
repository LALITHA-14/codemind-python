class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = ' '.join(word[::-1] for word in s.split())
        return reverse
        

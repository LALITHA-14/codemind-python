class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken=set(brokenLetters)
        words=text.split()
        c=0
        for word in words:
            if all(ch not in broken for ch in word):
                c+=1
        return c

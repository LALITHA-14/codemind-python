class Solution:
    def checkPangram(self,s):
        #code here
        pangram=set()
        for i in s.lower():
            if 'a'<=i<='z':
                pangram.add(i)
        return len(pangram)==26

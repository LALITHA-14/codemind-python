from collections import Counter
class Solution:
    def maximumFrequency(self, s):
        # Your Code goes here
        freq=Counter(s.split())
        max_values=max(freq.values())
        for word in freq:
             if freq[word]==max_values:
                 return f"{word} {max_values}"
                

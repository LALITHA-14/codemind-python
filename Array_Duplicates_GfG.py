from collections import Counter
class Solution:
    def findDuplicates(self, arr):
        freq = Counter(arr)
        duplicates = []
        for i in freq:
            if freq[i] > 1:
                duplicates.append(i)  
        return sorted(duplicates) if duplicates else []

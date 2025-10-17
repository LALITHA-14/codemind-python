class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mat=list(map(list,zip(*matrix)))
        return mat

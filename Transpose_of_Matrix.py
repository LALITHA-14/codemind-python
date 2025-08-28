class Solution:
    def transpose(self, mat):
        # code here
        mat=list(map(list,zip(*matrix)))
        return mat

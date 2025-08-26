class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_dia=0
        max_area=0
        for l,w in dimensions:
            dia=(l*l)+(w*w)
            area=l*w
            if dia>max_dia:
                max_dia=dia
                max_area=area
            elif dia==max_dia:
                max_area=max(max_area,area)
        return max_area

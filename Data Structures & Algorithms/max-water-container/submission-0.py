class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx = 0 
        p1 = 0 
        p2 = len(heights) - 1 
        while p1 < p2: 
            area = min(heights[p1],heights[p2]) * (p2-p1)
            maxx = max(area,maxx)
            if heights[p1] < heights[p2]:
                p1 = p1 + 1 
            else:
                p2 = p2 - 1 
        return maxx
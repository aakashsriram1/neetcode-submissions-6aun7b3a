class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0 
        right_max = 0
        total = 0 
        p1 = 0 
        p2 = len(height) - 1
        while p1 < p2: 
            if height[p2] >= height[p1]: 
                if height[p1] < left_max:
                    total += left_max - height[p1]
                else:
                    left_max = height[p1]
                p1 += 1
            else:
                if height[p2] < right_max:
                    total += right_max - height[p2]
                else:
                    right_max = height[p2]
                p2 -= 1
        return total 
                
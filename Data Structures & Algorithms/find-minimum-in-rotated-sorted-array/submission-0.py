class Solution:
    def findMin(self, nums: List[int]) -> int:
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2:
            middle = (p1+p2) // 2
            if nums[middle] > nums[p2]:
                p1 = middle + 1 
            else:
                p2 = middle 
        return nums[p1]
            
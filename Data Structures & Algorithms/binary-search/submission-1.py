class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0 
        p2 = len(nums) - 1 

        while p1 <= p2:
            mid = (p1 + p2) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                p2 = p2 - 1 
            else:
                p1 = p1 + 1     
        return -1 
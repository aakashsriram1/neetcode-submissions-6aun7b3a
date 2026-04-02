class Solution:
    def findMin(self, nums: List[int]) -> int:
        def condition(nums,index):
            return nums[index] <= nums[len(nums) - 1];

        lo = -1 
        hi = len(nums) 
        while lo+1 < hi:
            mid = (lo + (hi-lo)//2)
            if condition(nums,mid):
                hi = mid
            else:
                lo = mid
        
        return nums[hi] 


        
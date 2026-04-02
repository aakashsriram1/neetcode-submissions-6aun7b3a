class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #o(n^3) -> iterate 3 times to see if nums add up 
        #o(n^2) -> sort. iterate twice. first number + second part two sum 

        nums.sort()
        res = []
        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,1,2]
        for i in range(len(nums)): 
            p1 = i + 1 
            p2 = len(nums) - 1 
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            while p1 < p2: 
                total = nums[i] + nums[p1] + nums[p2]
                if total == 0: 
                    res.append([nums[i],nums[p1],nums[p2]])
                    p1 = p1 + 1 
                    p2 = p2 - 1  
                    while p2 + 1 < len(nums) and p1 < p2 and nums[p2] == nums[p2+1]:
                        p2 = p2 - 1
                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 = p1 + 1 
                if total > 0: 
                    p2 = p2 - 1 
                if total < 0: 
                    p1 = p1 + 1
                 
        return res

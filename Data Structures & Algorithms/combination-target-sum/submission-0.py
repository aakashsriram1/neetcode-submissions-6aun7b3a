class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #params = index and path 
        #constraints = total length -> len(nums)
        #choices -> choose current / skip current 
        #base case -> if curr_sum == target 

        res = []
        def backtrack(index,path,curr_sum):
            if curr_sum == target:
                res.append(path[:])
                return
            
            if curr_sum > target or index == len(nums):
                return 
            
            #choose current 
            path.append(nums[index])
            backtrack(index,path,curr_sum+nums[index])
            path.pop()
            #skip current
            backtrack(index+1,path,curr_sum)
        backtrack(0,[],0)
        return res
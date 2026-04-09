class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Base Case -> if index = len(nums) 
        # Choices -> take the number or skip the number 
        # Constraints -> None bc every subset is valid 
        # parameters -> index, path 


        res = []

        def backtrack(index,path):
            #basecase
            if index == len(nums):
                res.append(path[:])
                return
            
            #case 1
            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()

            #case 2 
            backtrack(index+1,path)

        backtrack(0,[])
        return res
            

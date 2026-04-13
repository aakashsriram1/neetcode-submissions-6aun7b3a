class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #at most once 

        # base case -> sum == target 
        # constraints -> each number can only be used once 
        # choices -> chose the number we are on or skip the number we are on 
        # parameters -> path, index, curr_sum 
        candidates.sort()
        res = []
        def backtrack(index,path,curr_sum):
            if curr_sum == target:
                res.append(path[:])
                return 
            if index == len(candidates) or curr_sum > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path,curr_sum+candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res
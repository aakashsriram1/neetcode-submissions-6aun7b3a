class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        maxx = 0 
        for i in nums: 
            count = 0 
            if (i-1) not in sett: 
                var = i 
                while var in sett: 
                    count = count + 1 
                    var = var + 1 
            maxx = max(count,maxx)
        return maxx

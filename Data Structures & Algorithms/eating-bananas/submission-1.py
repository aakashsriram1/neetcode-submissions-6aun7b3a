class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(piles,speed,maxx):
            time = 0 
            for i in range(len(piles)):
                time += math.ceil(piles[i] / speed)
                if time > maxx:
                    return False
            return True
        
        #minimum problem
        lo = 0
        hi = max(piles)
        while lo+1 < hi:
            mid = (lo + (hi-lo) // 2)
            if helper(piles,mid,h):
                hi = mid
            else:
                lo = mid 
        return hi

        


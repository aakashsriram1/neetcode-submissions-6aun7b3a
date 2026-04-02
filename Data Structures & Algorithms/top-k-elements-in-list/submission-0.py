class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute force 
        # -> hashmap of [value : frequency]
        # ie. [1:1, 2:2, 3:3]
        #sort in descending order 
        # append to output list as necessary 
        hashmap = {}
        for i in range(len(nums)): 
            hashmap[nums[i]] = hashmap.get(nums[i],0) + 1 

        heap = []
        for key, value in hashmap.items(): 
            heapq.heappush(heap,(value,key))
            if len(heap) > k: 
                heapq.heappop(heap)
        res = []
        for value, key in heap:
            res.append(key) 
        return res



        # more optimized 
        # build a min heap instead 
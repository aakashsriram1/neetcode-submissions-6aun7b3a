class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #min heap 
        #distance closest to 0
        #when heap bigger than k -> either append or pop
        heap = []
        for x,y in points:
            distance = x**2 + y**2
            heap.append([distance,x,y])
        heapq.heapify(heap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
            k = k - 1
        return res
        
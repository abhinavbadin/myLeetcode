class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #closest is nothing but nearest -> smallest -> so max heap

        maxheap = []
        
        for (x,y) in points:
            dist = math.sqrt((x*x) + (y*y))
            heapq.heappush(maxheap,(-dist,[x,y]))
            
            if len(maxheap) > k:
                heapq.heappop(maxheap)
            

        return [nums for dist,nums in maxheap]
import heapq as hp
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        maxHeap = [-x for x in stones]
        hp.heapify(maxHeap)

        while len(maxHeap) != 1:
            y = abs(hp.heappop(maxHeap))
            x = abs(hp.heappop(maxHeap))
            if x == y:
                hp.heappush(maxHeap,0)
            else:
                hp.heappush(maxHeap,-(y-x))
        return -maxHeap[0]
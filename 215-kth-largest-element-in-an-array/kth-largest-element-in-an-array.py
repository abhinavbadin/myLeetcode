import heapq as hp
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        hp.heapify(minHeap)
        while len(minHeap) > k:
            hp.heappop(minHeap)
        return minHeap[0]
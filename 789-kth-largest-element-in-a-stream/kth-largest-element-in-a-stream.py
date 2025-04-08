import heapq as hp
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        hp.heapify(self.minHeap)
        while len(self.minHeap) > k:
            hp.heappop(self.minHeap)  

    def add(self, val: int) -> int:
        hp.heappush(self.minHeap,val)
        if(len(self.minHeap) > self.k):
            hp.heappop(self.minHeap)
        return self.minHeap[0] 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
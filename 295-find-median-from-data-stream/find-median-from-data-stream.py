class MedianFinder:

    def __init__(self):
        self.left=[] #maxheap
        self.right=[] #minheap

    def addNum(self, num: int) -> None:
        #get the 2 heaps concept and now 
        #maxheap should contain max of left half(smaller)
        #minheap should contain min of right half(larger half)
        #because when even u split the array into 2 halfs(left and right)
        #in that larger of left half and smaller of right average is median
        #by balancing 2 heaps difference mostly by 1 find the median

        heapq.heappush(self.left,-num)
        
        # Move the largest from left to right if out of order
        if self.right and (-self.left[0] > self.right[0]):
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        #handling the differences
        if len(self.left) > len(self.right) + 1: #if difference is greater than 1
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right,val)
        elif len(self.right) > len(self.left): #at any point we should not make right > left
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)


    def findMedian(self) -> float:
        if len(self.left) != len(self.right):
            return float(-self.left[0])
        
        return (-self.left[0] + self.right[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
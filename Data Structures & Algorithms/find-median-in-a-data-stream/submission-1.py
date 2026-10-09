import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush_max(self.max_heap,num)
        elif num > self.max_heap[0]:
            heapq.heappush(self.min_heap,num)
        else :
            heapq.heappush_max(self.max_heap,num)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            value = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, value)

        elif len(self.min_heap) > len(self.max_heap):
            value = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, value)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] + self.min_heap[0])/2
        else :
            return self.max_heap[0]
        
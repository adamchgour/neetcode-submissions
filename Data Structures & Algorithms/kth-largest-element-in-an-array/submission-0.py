import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap =  []
        heapq.heapify(heap)

        for _ , val in enumerate(nums):
            if len(heap) < k :
                heapq.heappush(heap,val)
            else :
                if val > heap[0] :
                    heapq.heappop(heap)
                    heapq.heappush(heap,val)
    
        return heap[0]

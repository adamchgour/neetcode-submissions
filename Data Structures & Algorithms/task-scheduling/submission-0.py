import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = list(count.values())
        heapq.heapify_max(maxHeap)

        q = deque() # (remaining_count, available_time)

        time = 0
        
        while q or maxHeap :
            time += 1

            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) - 1

                if cnt > 0:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                cnt, _ = q.popleft()
                heapq.heappush_max(maxHeap, cnt)

        return time
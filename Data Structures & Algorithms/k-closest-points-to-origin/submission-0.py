import heapq
from math import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x1,y1,x2,y2):
            return sqrt((x1-x2)**2 + ((y1-y2)**2))

        knn = []
        heapq.heapify_max(knn)

        for i in range(len(points)):
            if i < k :
                heapq.heappush_max(knn,(dist(0,0,points[i][0],points[i][1]),points[i]))
            else :
                if dist(0,0,points[i][0],points[i][1]) <= knn[0][0] :
                    heapq.heappop_max(knn)
                    heapq.heappush_max(knn,(dist(0,0,points[i][0],points[i][1]),points[i]))
        
        return [knn[i][1] for i in range(k)]

        
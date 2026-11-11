class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = [0]*(len(cost)+1)

        for i in range(2,len(cost)+1):
            L[i] = min(L[i-1] + cost[i-1],L[i-2] + cost[i-2])
        
        return L[-1]
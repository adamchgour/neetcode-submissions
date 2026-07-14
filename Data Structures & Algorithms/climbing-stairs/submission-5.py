class Solution:
    def climbStairs(self, n: int) -> int:
        d = {1:1,2:2}
        for i in range(3,n+1):
            if i not in d.keys():
                d[i] = d[i-1] + d[i-2]
        
        return d[n]
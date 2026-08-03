class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)
        out = maxi
        left , right = 1, maxi

        while left <= right :
            mid = (left + right) // 2
            count = 0
            
            for i in range(len(piles)):
                count += math.ceil(piles[i] / mid)

            if count > h :
                left = mid + 1
            elif count <= h :
                right = mid - 1
                if mid < out :
                    out = mid
        return out
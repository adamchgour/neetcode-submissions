class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        L , R = 0,len(heights)-1
        
        while L < R :
            s = min(heights[L],heights[R])*(R-L)
            if s > maxi:
                maxi = s
            if heights[L] >= heights[R]:
                R -= 1
            else :
                L += 1
        return maxi
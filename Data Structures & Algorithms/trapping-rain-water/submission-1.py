class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        l_max = 0
        r_max = 0
        area = 0

        while l < r :
            if height[l] <= height[r]:
                l_max = max(l_max, height[l])
                area += l_max - height[l]
                l += 1
            if height[l] > height[r]:
                r_max = max(r_max,height[r])
                area += r_max - height[r]
                r -= 1

        return area


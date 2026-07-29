class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack_l = []
        stack_r =[]
        L = len(heights) * [-1]
        R = len(heights) * [len(heights)]
        maxi = 0

        for i in range(len(heights)): 
            while stack_r and heights[i] < heights[stack_r[-1]]:
                idx = stack_r.pop()
                R[idx] = i
            stack_r.append(i)
        for i in range(1,len(heights)+1):
            j = len(heights) - i
            while stack_l and heights[j] < heights[stack_l[-1]]:
                idx = stack_l.pop()
                L[idx] = j
            stack_l.append(j)
        
        for i in range (len(heights)) :
            if (R[i]-L[i]-1)*heights[i] > maxi :
                maxi = (R[i]-L[i]-1)*heights[i]
        
        return maxi
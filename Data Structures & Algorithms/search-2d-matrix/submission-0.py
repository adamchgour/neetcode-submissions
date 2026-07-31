class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right = 0,len(matrix[0]) - 1
        top, bot = 0,len(matrix) - 1
        i = -1

        while top <= bot :
            mid = (top + bot) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1] :
                i = mid
                break
            elif target > matrix[mid][-1] :
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1

        if i == -1 :
            return False
        
        while left <= right :
            mid = (left + right) // 2

            if target == matrix[i][mid] :
                return True
            elif target > matrix[i][mid] :
                left = mid + 1
            else :
                right = mid - 1
            
        return False
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L , R = 0 , len(numbers)
        
        while R > L:
            if numbers[L]+numbers[R-1] == target:
                return [L+1,R]
            elif numbers[L]+numbers[R-1] > target :
                R -= 1
            else :
                L += 1

                
                
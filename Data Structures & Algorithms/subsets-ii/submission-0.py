class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        def backtrack(index,path):
            if index == len(nums):
                result.append(path[:])
                return
            
            path.append(nums[index])    
            backtrack(index + 1,path)
            path.pop()

            i = index
            while i<len(nums) and nums[i] == nums[index]:
                i+= 1
            backtrack(i,path)

        backtrack(0,[])
        return result
                
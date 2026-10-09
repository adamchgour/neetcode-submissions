class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index,path,remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(index,len(nums)):
                num = nums[i]
                if num > remaining :
                    continue
                path.append(num)
                backtrack(i, path,remaining-num)
                path.pop()
        
        backtrack(0,[],target)
        return result
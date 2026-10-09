class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(index,path,remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(index,len(candidates)):
                num = candidates[i]
                if i > index and num == candidates[i-1]:
                    continue
                if num > remaining :
                    break
                path.append(num)
                backtrack(i+1, path,remaining-num)
                path.pop()
        
        backtrack(0,[],target)
        return result
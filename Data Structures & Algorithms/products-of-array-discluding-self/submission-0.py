class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            L = []
            for i,_ in enumerate(nums):
                p = 1
                for j,m in enumerate(nums):
                    if i != j:
                        p = p*m
                L.append(p)
            return L
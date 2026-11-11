class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        L = [0]*n

        L[0] = nums[0]
        L[1] = max(nums[0], nums[1])

        for i in range(2,n):
            L[i] = max(L[i-2] + nums[i],L[i-1])

        return L[-1]
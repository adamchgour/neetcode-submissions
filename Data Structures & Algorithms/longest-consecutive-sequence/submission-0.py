class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        basket = set(nums)
        max_len = 0

        for elt in basket:
            if elt - 1 not in basket:
                length = 1
                x = elt
                while x + 1 in basket:
                    x += 1
                    length += 1
                max_len = max(max_len, length)

        return max_len
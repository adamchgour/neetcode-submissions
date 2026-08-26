class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        h = {}
        length = 0

        for r, char in enumerate(s):
            if char in h:
                l = max(l, h[char] + 1)

            h[char] = r
            length = max(length, r - l + 1)

        return length
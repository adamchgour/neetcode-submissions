class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        h = {}
        length = 0
        while r < len(s):
            if (s[r] not in h) or h[s[r]] < l:
                h[s[r]] = r
                length = max(length,r-l+1)
                r += 1
            else : 
                l = 1 + h[s[r]]
        return length
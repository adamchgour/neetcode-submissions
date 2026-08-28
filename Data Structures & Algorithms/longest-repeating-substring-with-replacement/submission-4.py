class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        h = {}
        length = 0
        max_freq = 0
        
        while r < len(s):
            if s[r] not in h:
                h[s[r]] = 1
                max_freq = max(max_freq, h[s[r]])
            else:
                h[s[r]] += 1
                max_freq = max(max_freq, h[s[r]])
            count = (r-l+1) - max_freq
            while count > k:
                h[s[l]] -= 1
                l += 1 
                count = (r-l+1)-max_freq
            length = max(length,r-l+1)
            r += 1
        return length     
            

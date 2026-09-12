class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = {}
        h2 = {}
        n1 = len(s1)
        n2 = len(s2)
        l,r = 0,0

        for elt in s1:
            if elt in h1:
                h1[elt] += 1 
            else :
                h1[elt] = 1
        
        while r < n2:
            if r-l < n1:
                if s2[r] in h2:
                    h2[s2[r]] += 1
                else :
                    h2[s2[r]] = 1
                r += 1
            else :
                h2[s2[l]] -= 1
                if h2[s2[l]]==0:
                    del h2[s2[l]]
                l += 1
            
            if h1 == h2:
                return True
        
        return False

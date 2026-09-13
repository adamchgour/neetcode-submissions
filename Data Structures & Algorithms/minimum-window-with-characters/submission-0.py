class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ht = {} #have
        hs = {} #need
        have = 0
        l,r = 0,0
        mini = [0,len(s),False]

        for elt in t:
            if elt in ht:
                ht[elt] += 1
            else :
                ht[elt] = 1

        need = len(ht)

        while r < len(s) or have == need:

            if need != have:
                if s[r] in ht :
                    if s[r] in hs:
                        hs[s[r]] += 1
                    else :
                        hs[s[r]] = 1
                    if  ht[s[r]] == hs[s[r]]:
                        have += 1  
                r += 1
            else :
                if s[l] in ht :
                    if hs[s[l]] == ht[s[l]]:
                        have -= 1
                    hs[s[l]] -= 1
                if (r-l <= mini[1]-mini[0]):
                    mini = [l,r,True]
                l += 1  

        if mini[2]:
            return s[mini[0]:mini[1]]
        else:
            return ""
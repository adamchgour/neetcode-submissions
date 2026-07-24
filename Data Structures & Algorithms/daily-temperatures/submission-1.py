class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        L = []
        for i,elt in enumerate(temperatures):
            c = i+1
            while (c < len(temperatures)) and (elt >= temperatures[c]):
                c += 1
            if c == len(temperatures) :
                c = i
            L.append(c-i)
        return L
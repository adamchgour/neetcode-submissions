class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        L = len(temperatures) * [0]

        for i in range(1,len(temperatures)): 
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                L[idx] = i-idx
            stack.append(i)
        return L
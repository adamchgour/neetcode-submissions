class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        L = len(temperatures) * [0]

        for i in range(1,len(temperatures)):
            temp = temperatures[i]
            while stack != [] and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                top = temperatures[idx]
                L[idx] = i-idx
            stack.append(i)
        return L
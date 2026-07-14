class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L = []
        d = {}
        for i in range(len(nums)):
            if nums[i] in d.keys():
                d[nums[i]] += 1
            else :
                d[nums[i]] = 1
        for i in range(k):
            max_value = max(d.values())
            cles = [j for j, v in d.items() if v == max_value]
            L.append(cles[0])
            del d[cles[0]]
        return L
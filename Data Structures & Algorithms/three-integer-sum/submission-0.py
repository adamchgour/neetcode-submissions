class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        out = []

        for M,target in enumerate(nums):
            L , R = M+1 , len(nums) - 1

            if M > 0 and nums[M] == nums[M-1]:
                continue
            else :

                while R > L:
                    s = nums[L] + nums[R]
                    if s == -target:
                        out.append([nums[L],nums[R],nums[M]])

                        L += 1
                        R -= 1
                        while L < R and nums[L] == nums[L-1]:
                            L += 1
                        while L < R and nums[R] == nums[R+1]:
                            R -= 1  
                
                    elif s > -target :
                        R -= 1
                    else :
                        L += 1
        return out

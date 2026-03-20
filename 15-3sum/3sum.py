class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for index, num in enumerate(nums):
            if num == nums[index-1] and index>0:
                continue
            left = index+1
            right = len(nums)-1
            while left<right:
                if num + nums[left] + nums[right] == 0:
                    res.append([num,nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]: left+=1
                    while left<right and nums[right]==nums[right-1]: right-=1
                    left+=1
                    right-=1
                elif num + nums[left] + nums[right] > 0:
                    right-=1
                else:
                    left+=1
        return res
                
        
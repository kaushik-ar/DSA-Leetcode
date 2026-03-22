from collections import deque
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # if len(nums) == 100000:
        #     if nums[0] == -100000000:
        #         return 2
        #     return 100000
        numset = set(nums)
        max_length = 0
        for num in numset:
            if num-1 not in numset:
                length = 1
                curr = num
                while curr+1 in numset:
                    length += 1
                    curr += 1
                max_length = max(max_length, length)
        return max_length


        
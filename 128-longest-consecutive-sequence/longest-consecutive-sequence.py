from collections import deque
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        max_length = 0
        for num in numSet:
            if num-1 not in numSet:
                length = 0
                temp = num
                while temp in numSet:
                    length+=1
                    temp+=1
                max_length = max(length, max_length)
        return max_length
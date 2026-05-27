from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for num, freq in count.items():
            if freq > (len(nums)//2):
                res = num
        return res
            

        
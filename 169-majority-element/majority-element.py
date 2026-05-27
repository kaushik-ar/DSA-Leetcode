from collections import Counter, defaultdict
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        frequency = defaultdict(list)
        for num, freq in count.items():
            frequency[freq].append(num)
        res = []
        for freq, num in frequency.items():
            if freq > math.floor(len(nums)/2):
                res.append(num[0])

        return res[0]
            

        
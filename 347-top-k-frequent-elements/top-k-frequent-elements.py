from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res

        


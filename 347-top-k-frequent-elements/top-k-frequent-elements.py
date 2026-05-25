from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        bucket = defaultdict(list)
        for num in nums:
            count[num] +=1
        for num, freq in count.items():
            if bucket[freq] == []:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            if i in bucket:

                for j in bucket[i]:
                    res.append(j)
                    if len(res)==k:
                        return res

        return res







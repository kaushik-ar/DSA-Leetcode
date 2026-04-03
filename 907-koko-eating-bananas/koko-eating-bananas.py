class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check_k(k : int) -> bool:
            hrs = 0
            for p in piles:
                hrs += ceil( p/k)
            return hrs <= h

        l = 1
        r = max(piles)
        while l < r:
            mid = (l+r)//2
            if check_k(mid):
                r = mid
            else:
                l = mid + 1
        return r

           
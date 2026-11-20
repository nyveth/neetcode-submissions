import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        

        while l < r:
            mid = l + (r - l) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
            
            if total_hours > h:
                l = mid + 1
            else:
                r = mid

        return r
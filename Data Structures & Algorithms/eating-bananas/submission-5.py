class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        res = maxK

        l, r = 1, maxK

        while l <= r:
            med = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / med)
            
            if time <= h:
                res = min(res, med)
                r = med - 1
            else:
                l = med + 1
        
        return res
            
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles) # lowest hours as this is the highest rate
        res = maxPile

        low, high = 1, maxPile

        while low <= high:
            med = (low + high) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / med)
            
            if time <= h:
                res = min(res, med)
                high = med - 1
            
            else:
                low = med + 1
        
        return res
        
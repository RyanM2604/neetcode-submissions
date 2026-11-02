class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Need to find a function that with input rate, gives feasible in hours

        # rate == 1, 10 hours > 9hrs so False
        # rate == 2, 6 hours < 9hrs so True
        # rate == 3, 5 hours < 9hrs so True

        # Highest rate will be the largest pile which means hours taken is len(piles)


        low = 1
        high = max(piles)  
        res = float('inf')  

        while low <= high:
            mid = (low + high) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return res
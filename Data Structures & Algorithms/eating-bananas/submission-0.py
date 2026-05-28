class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isEatable(k: int,piles: List[int], h: int):
            Eatsum = 0
            for i in piles: 
                Eatsum+= math.ceil(i / k)
            if Eatsum <= h: 
                return True
            else:
                return False

        low, hi = 1, max(piles)
        res = hi

        while low <= hi: 
            mid = low + (hi - low) // 2
            
            if isEatable(mid, piles, h): 
                hi = mid - 1
                res = min(mid, res)
            else: 
                low = mid + 1
        
        return res


        
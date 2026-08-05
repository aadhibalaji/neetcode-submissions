class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        bestRate = right

        while left <= right:
            current = (left + right) // 2

            time = 0

            for p in piles:
                time += math.ceil(float(p) / current)

            if time <= h:
                bestRate = current
                right = current - 1
            else:
                left = current + 1

          
        
        return bestRate
            
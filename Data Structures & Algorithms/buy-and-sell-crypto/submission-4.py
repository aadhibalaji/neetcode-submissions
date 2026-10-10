class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        buy = prices[0]

        res = 0

        for price in prices:
            if buy > price:
                buy = price

            profit = price - buy

            res = max(res, profit)

        return res
            

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        bestProfit = 0
        for i in range(len(prices)):
            if (prices[i] <= buy):
                buy = prices[i]
            
            profit = prices[i] - buy

            if (profit > bestProfit):
                bestProfit = profit
    
        return bestProfit

            

            
            
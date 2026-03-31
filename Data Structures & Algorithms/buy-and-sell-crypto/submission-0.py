class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float('inf')
        maxP=0
        for price in prices:
            minP=min(minP,price)
            profit=price-minP
            maxP=max(maxP,profit)
        return maxP
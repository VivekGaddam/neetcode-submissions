class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        sol=0
        for i in range(1,len(prices)):
            
            sol=max(sol,prices[i]-mini)
            mini=min(mini,prices[i])
        return sol
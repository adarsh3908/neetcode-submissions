class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        cur = prices[0]
        for i in prices:
            m = max(m,i-cur)
            cur = min(i,cur)

        return m    
        
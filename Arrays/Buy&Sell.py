class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = prices[0]
        max_profit = 0

        for price in prices:

            if price < lowest:
                lowest = price

            profit = price - lowest   

            max_profit = max(max_profit,profit) 
        
        return max_profit    

solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices))  # Output: 5
      
        
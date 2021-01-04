class Solution:
    def maxProfit(self, prices):
        res = 0
        minValue = float("inf")
        for i in range(len(prices)):
            if prices[i] < minValue:        #更新最小值
                minValue = prices[i]
            if prices[i] - minValue > res:  #更新最大收益
                res = prices[i] - minValue
        return res
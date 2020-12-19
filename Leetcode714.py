"""
买卖股票的最佳时机含手续费
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

贪心

基本思路：
维护 buy sell prices profit 三个数组
循环判断每次最合适的价格 不断循环

动态规划

基本思路：1.写出状态转移方程
         2.规定手续费在买入时产生
         3.维护一个数组 0表示不持有 1表示持有 不断对其迭代更新 len(prices)
         4.最优解产生在不持股的时候

"""
class Solution1:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell = buy = prices[0]
        profit = 0
        for x in prices:
            if buy < sell-fee:                #赚钱的情况
                if x < sell-fee:
                    profit += (sell-buy-fee)
                    sell = buy = x
                elif x > sell:
                    sell = x
            else:                            #目前的价格大于买入价格
                if x > sell:
                    sell = x
                if x < buy:
                    sell = buy = x
        if buy < sell - fee:
            profit += (sell-buy-fee)
        return profit




class Solution2:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0  # 交易天数小于2，无法完成一次完整的买入-卖出

        dp = [0, 0]   # 维持一个滚动数组，因为当天状态继承于上一天
        dp[1] = -prices[0]-fee # 第一天持股，证明刚买入股票，计算持股成本

        for i in range(1, n):
            dp[0] = max(dp[0], dp[1]+prices[i])  # 上轮持股利润和不持股利润
            dp[1] = max(dp[1], dp[0]-prices[i]-fee)

        return dp[0]  # 最优解一定是不持股的时候，因为持股会花钱

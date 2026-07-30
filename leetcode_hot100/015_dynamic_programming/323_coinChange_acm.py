class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [inf]*(amount+1)
        dp[0] = 0
        n = len(coins)
        for i in range(amount+1):
            for j in range(n):
                if i >= coins[j]:
                    dp[i] = min(dp[i],dp[i-coins[j]]+1)
        if dp[amount] == inf:
            return -1
        else:
            return dp[amount]
       
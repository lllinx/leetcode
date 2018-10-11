"""

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1
"""
# bottom up solution
def coinChange(coins,amount):
	dp=[amount+1 for _ in range(amount+1)]
	dp[0]=0
	for i in range(1,amount+1):
		for j in range(len(coins)):
			if i>=coins[j]:
				dp[i]=min(dp[i],dp[i-coins[j]]+1)
	if dp[amount]>amount:
		return -1
	return dp[amount]

	

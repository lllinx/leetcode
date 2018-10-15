"""

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""

# dynamic programming
def numSquares(n):
	dp=[n+1 for _ in range(n+1)]
	dp[0]=0

	for i in range(1,n+1):
		for j in range(1,n+1):
			if j*j<=i:
				dp[i]=min(dp[i],dp[i-j*j]+1)
			else:
				break
	if dp[n]==n+1:
		return -1
	return dp[n]

# could also use BFS





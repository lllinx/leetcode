"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

def maximalSquare(matrix):
	maxi=0
	dp=matrix[:]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if i==0 or j==0 or matrix[i][j]=="0":
				dp[i][j]=int(matrix[i][j])
			elif matrix[i][j]=="1":
				dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
			maxi=max(maxi,dp[i][j])
	return maxi*maxi

	
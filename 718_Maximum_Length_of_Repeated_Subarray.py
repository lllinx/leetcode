"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].

Note:

    1 <= len(A), len(B) <= 1000
    0 <= A[i], B[i] < 100
"""

def findLength(A, B):
	dp=[[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
	for i in range(len(A)-1,-1,-1):
		for j in range(len(B)-1,-1,-1):
			if A[i]==B[j]:
				dp[i][j]=dp[i+1][j+1]+1
	return max(max(row) for row in dp)



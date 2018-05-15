"""
dynamic programming
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
def maxsubarray(nums):
	dp=[0 for _ in range(len(nums))]
	dp[0]=nums[0]
	answer=dp[0]
	for i in range(len(nums)):
		if dp[i-1]>0:
			dp[i]=dp[i-1]+nums[i]
		else:
			dp[i]=nums[i]
		answer=max(answer,dp[i])
	return answer
	


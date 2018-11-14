"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

def lengthOfLIS(nums):
	if len(nums)==0:
		return 0
	dp=[0 for i in range(len(nums))]
	dp[0]=1
	ans=dp[0]

	for i in range(1,len(nums)):
		maxval=0
		for j in range(i):
			if nums[i]>nums[j]:
				maxval=max(maxval,dp[j])
		dp[i]=maxval+1
		ans=max(ans,dp[i])
	return ans





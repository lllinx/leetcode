"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

def maxProduct(nums):
	result=nums[0]
	maxs, mins=result, result
	for i in range(1,len(nums)):
		if nums[i]<0:
			maxs, mins=mins, maxs
		maxs=max(nums[i], nums[i]*maxs)
		mins=min(nums[i], nums[i]*mins)
		result=max(result, maxs)

	return result



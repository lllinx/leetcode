"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
Input=[-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	length=range(1,len(nums)+1)
	result=[]
	for i in length:
		for j in range(len(nums)-i):
			s=sum(nums[j:j+i+1])
			result.append(s)
	return max(result)


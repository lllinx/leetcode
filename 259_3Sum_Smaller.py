"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]

Follow up: Could you solve it in O(n2) runtime?
"""

def threeSumSmaller(nums,target):
	nums.sort()
	result=0
	for i in range(len(nums)):
		tar=target-nums[i]
		low,high=i+1,len(nums)-1
		while low<high:
			if nums[low]+nums[high]<tar:
				result+=high-low
				low+=1
			else:
				high-=1
	return result
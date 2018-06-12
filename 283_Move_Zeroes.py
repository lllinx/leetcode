"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
def movezeros(nums):
	times,i=0,0
	while times<len(nums):
		if nums[i]==0:
			nums.pop(i)
			nums.append(0)
			i+=1
		times+=1

def movezeros2(nums):
	i,non_zero=0,0
	length=len(nums)
	while i<length:
		if nums[i]!=0:
			nums[non_zero]=nums[i]
			non_zero+=1
		i+=1

	while non_zero<len(nums):
		nums[non_zero]=0
		non_zero+=1
	return nums






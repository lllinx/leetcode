"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
"""

def triangleNumber(nums):
	nums.sort()
	count=0
	for i in range(len(nums)-1,1,-1):
		l,r=0,i-1
		while l<r:
			if nums[l]+nums[r]>nums[i]:
				count+=r-l
				r-=1
			else:
				l+=1
	return count

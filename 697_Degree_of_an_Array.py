"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:

Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:

Input: [1,2,2,3,1,4,2]
Output: 6
"""

def findShortestSubArray(nums):
	dic={}
	for i in range(len(nums)):
		if nums[i] not in dic:
			dic[nums[i]]=[1,i,i]
		else:
			dic[nums[i]][0]+=1
			dic[nums[i]][2]=i
	result=None
	max1=0
	for v in dic.values():
		if v[0]>max1:
			max1=v[0]
			result=v[2]-v[1]+1
		elif v[0]==max1:
			result=min(result,v[2]-v[1]+1)
	return result



















"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
def majorityelement(nums):
	result={}
	for element in nums:
		if element not in result.keys():
			result[element]=1
		else:
			result[element]+=1
	return [res for res in result.keys() if result[res]>len(nums)/3]

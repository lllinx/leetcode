"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
"""

def largestNumber(nums):
	nums=[str(x) for x in nums]
	longest=max([len(x) for x in nums])
	nums.sort(key=lambda x:x*(longest//len(x)+1),reverse=True)
	if nums and nums[0]=="0":
		return "0"
	return "".join(nums)

	
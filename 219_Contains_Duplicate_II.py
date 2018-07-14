"""
Given an array of integers and an integer k, 
find out whether there are two distinct indices i and j 
in the array such that nums[i] = nums[j] and the absolute 
difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

def containsNearbyDuplicate(nums,k):
	"""
	using dictionary
	"""
	dic={}
	for i in range(len(nums)):
		if nums[i] not in dic:
			dic[nums[i]]=i
		else:
			if i-dic[nums[i]]<=k:
				return True
			else:
				dic[nums[i]]=i
	return False

def containsNearbyDuplicate2(nums,k):
	"""
	using set
	"""
	set1=set()
	for i in range(len(nums)):
		if nums[i] in set1:
			return True
		set1.add(nums[i])
		if len(set1)>k:
			set1.remove(nums[i-k])
	return False
















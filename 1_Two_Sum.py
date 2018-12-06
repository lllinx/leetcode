"""1. Two Sum
given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

since this question requires that
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
The first answer does not fit
"""
	# for i in range(len(nums)):
	# 	for j in range(i+1,len(nums)):
	# 		if nums[i] + nums[j] == target:
	# 			return [i,j]
	# 		j += 1
	# 	i += 1

	# for i in range(len(nums)):
	# 	other=target-nums[i]
	# 	if other in nums:
	# 		j=nums.index(other)
	# 		if i!=j:
	# 			return [i,j]
	# 	i+=1
def twoSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	dic={}
	for i in range(len(nums)):
		if target-nums[i] in dic.keys():
			return [dic[target-nums[i]],i]
		else:
			dic[nums[i]]=i




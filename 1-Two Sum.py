"""1. Two Sum"""
# given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
def twoSum(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	for i in range(0,len(nums)):
		for j in range(i+1,len(nums)):
			if nums[i] + nums[j] == target:
				return [i,j]
			j += 1
		i += 1
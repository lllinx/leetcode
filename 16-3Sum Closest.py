def threesum(nums):
	nums.sort()
	result=[]
	for i in range(len(nums)-2):
		if nums[i]>0:
			break
		if i>=1 and nums[i]==nums[i-1]:
			continue
		target=-nums[i]
		l,r=i+1,len(nums)-1
		while l<r:
			if nums[l]+nums[r]==target:
				result.append([nums[i],nums[l],nums[r]])
				while l<r and nums[l+1]==nums[l]:
					l+=1
				while l<r and nums[r-1]==nums[r]:
					r-=1
				l+=1
				r-=1
			elif nums[l]+nums[r]<target:
				while nums[l+1]==nums[l]:
					l+=1
				l+=1
			else:
				while nums[r-1]==nums[r]:
					r-=1
				r-=1
	return result
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
def threesumclosest(nums,target):
	nums.sort()
	first_3=nums[0]+nums[1]+nums[2]
	last_3=nums[-1]+nums[-2]+nums[-3]
	if target<first_3:
		return first_3
	elif target>last_3:
		return last_3
	result=first_3
	for i in range(len(nums)-2):
		l,r=i+1,len(nums)-1
		while l<r:
			curr_sum=nums[i]+nums[l]+nums[r]
			if curr_sum==target:
				return target
			if abs(curr_sum-target)<abs(result-target):
				result=curr_sum
			elif curr_sum>target:
				while l<r and nums[r-1]==nums[r]:
					r-=1
				r-=1
			else:
				while l<r and nums[l+1]==nums[l]:
					l+=1
				l+=1

	return result





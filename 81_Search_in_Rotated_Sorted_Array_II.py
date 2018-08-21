"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

"""

def search(nums,target):
	l,r=0,len(nums)-1
	while l<=r:
		mid=(l+r)//2
		if nums[mid]==target:
			return True
		if nums[l]==nums[mid] and nums[r]==nums[mid]:
			l+=1
			r-=1
		elif nums[l]<=nums[mid]:
			if target>=nums[l] and target<nums[mid]:
				r=mid-1
			else:
				l=mid+1
		else:
			if target>nums[mid] and target<=nums[r]:
				l=mid+1
			else:
				r=mid-1
	return False








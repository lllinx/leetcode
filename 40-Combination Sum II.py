"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

def combinationsum2(nums,target):
	nums.sort()
	result=[]
	def dfs(nums,target,index,path,res):
		if target==0:
				res.append(path[:])
		for i in range(index,len(nums)):
			if target<nums[i]:
				break
			elif i>index and nums[i]==nums[i-1]:
				continue
			else:
				path.append(nums[i])
				dfs(nums,target-nums[i],i+1,path,res)
				path.pop()
	dfs(nums,target,0,[],result)
	return result







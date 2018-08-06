"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

def subsetsWithDup(nums):
	res=[]
	nums.sort()
	def dfs(nums,index,temp,res):
		res.append(temp[:])
		for i in range(index,len(nums)):
			if i>index and nums[i]==nums[i-1]:
				continue
			temp.append(nums[i])
			dfs(nums,i+1,temp,res)
			temp.pop()
	dfs(nums,0,[],res)
	return res







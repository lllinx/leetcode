"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

def subsets(nums):
	res=[]
	def dfs(nums,index,temp,res):
		res.append(temp[:])
		for i in range(index,len(nums)):
			temp.append(nums[i])
			dfs(nums,i+1,temp,res)
			temp.pop()
	dfs(nums,0,[],res)
	return res











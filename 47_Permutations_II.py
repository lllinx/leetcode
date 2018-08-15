"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

def permuteUnique(nums):
	res=[]
	used=[False for n in nums]
	nums.sort()

	def dfs(nums,temp,used,res):
		if len(temp)==len(nums):
			res.append(temp[:])
			return
		for i in range(len(nums)):
			if used[i]:
				continue
			if i>0 and nums[i]==nums[i-1] and not used[i-1]:
				continue
			temp.append(nums[i])
			used[i]=True
			dfs(nums,temp,used,res)
			temp.pop()
			used[i]=False
		return res
	dfs(nums,[],used,res)
	return res






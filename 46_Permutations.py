"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

def permute(nums):
	res=[]
	def dfs(num,temp,res,k):
		if len(temp)==k:
			res.append(temp[:])
			return
		for i in range(len(num)):
			if num[i] in temp:
				continue
			else:
				temp.append(num[i])
				dfs(num,temp,res,k)
				temp.pop()
		return res
	dfs(nums,[],res,len(nums))
	return res









"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""

def combine(n,k):
	res=[]
	def dfs(n,start,k,res,temp):
		if len(temp)==k:
			res.append(temp[:])
			return
		for i in range(start,n+1):
		# for i in range(start,n-k+len(temp)+2):
			temp.append(i)
			dfs(n,i+1,k,res,temp)
			temp.pop()
	dfs(n,1,k,res,[])
	return res


